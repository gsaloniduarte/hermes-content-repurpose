# Changelog

Reverse-chronological record of structural work in this repo. Newest first.
Per `README.md` rule 2, agents append here in the same task that changes the
layout or behaviour.

---

## 2026-10-02 - Morning briefing vai para o topico Daily

### Entrega

`scripts/hermes-morning-briefing.py`:

- `CHAT_ID`: `7460792441` (DM) -> **`-1004348330719`** (grupo **HERMES DEFAULT**)
- novo `MESSAGE_THREAD_ID = 19` (topico **Daily**)
- `send_telegram()` passou a enviar `message_thread_id`

`cron/jobs.json`: `deliver` `local` -> `origin`, com `thread_id: 19`.

Backups: `*.bak-antes-thread19` no script e no `jobs.json`.

### Prompt do job tambem foi corrigido

**Este era o bug real.** O job tem dois mecanismos: o script **e** um prompt de agente.
Eu so tinha limpo o script. O prompt dizia *"check calendar, email, models, job hunting
context"*, e o agente reescrevia o relatorio com LinkedIn e candidaturas — verificado em
execução real as 15:55, que saiu com secao *LinkedIn Automation* e 28 URLs de
`applied_jobs.txt`.

Prompt novo: manda executar o script e proibe explicitamente adicionar job hunting,
LinkedIn, candidaturas ou busca de vagas. Backup `jobs.json.bak-antes-prompt-limp`.

Re-executado as 15:56: relatorio saiu limpo — calendar, email, modelos, AI summary,
proximos passos. Nenhuma mencao a LinkedIn ou job hunting.

### Model Routing Score Update — NAO alterado (pendente)

O destino pedido foi `t.me/c/4348330719/1`. **Esse topico nao existe.**

Sondagem no grupo `-1004348330719` (HERMES DEFAULT): threads que aceitam escrita
do bot sao apenas **2 (IDEIAS)** e **19 (Daily)**. Threads 1, 3-18 e 20-25 retornam
*message thread not found*. O bot e `member`, nao admin, entao nao consegue criar topicos
(*not enough rights to create a topic*).

O Model Routing continua delivering em `telegram:-5401894759` (**HERMES - MODELS**).

### Observacao sobre nomes de grupo

O grupo `-1004348330719` aparece em registros antigos como *Hermes - Buscador de Conteudo*
e agora se chama **HERMES DEFAULT**. O ID e o mesmo — o grupo foi renomeado. Por isso o
`automation-ideas` continua funcionando no mesmo lugar.

### Entrega `delivery_failed` no teste

`last_status: delivery_failed`, erro *Telegram send failed: Timed out*. **Foi a rede**, nao
a configuracao: o envio direto via Bot API no thread 19 funcionou segundos antes, e o
gateway registrou as 650 linhas de `ConnectTimeout` da API do Telegram ao longo do dia.
`failure_streak: 0`, proximo disparo 03/10 08:00.

---
## 2026-10-01 (fim de dia 6) - ajustes nos jobs das 08:00

### Morning briefing - removido o bloco de job hunting

A pedido do usuario. Tres pontos alterados em `scripts/hermes-morning-briefing.py`:

- secao **Job Hunting** removida
- **job hunting** removido do contexto do prompt de IA
- proximos passos: *verificar deadlines de aplicacoes* / *revisar respostas LinkedIn*
  substituidos por *revisar e-mails importantes*

Backup: `scripts/backups/config/hermes-morning-briefing.py.bak-antes-jobs-20261001`

### automation-ideas - entrega movida para o topico IDEIAS

**Causa raiz:** o grupo `Hermes - Buscador de Conteudo` virou **supergroup**.
O `chat_id` antigo (`-5424672709`) passou a responder
*group chat was upgraded to a supergroup chat*. O job estava quebrado por isso.

- `chat_id`: `-5424672709` -> **`-1004348330719`** (supergroup)
- `message_thread_id`: novo parametro -> **2** (topico IDEIAS)
- `send_telegram()` ganhou o parametro opcional `thread_id`
- `cron/jobs.json`: `origin.thread_id` = 2 (backup `.bak-antes-topico-ideias`)

Como o topico foi achado: o link `t.me/c/4348330719/2` nao era grupo+tema,
era **grupo + numero da mensagem**. O `/2` final era a pista do `message_thread_id`.
Sondagem confirmou: thread 1 = *message thread not found*, thread 2 = aceito.

**Limite conhecido:** o bot e `member`, nao admin. Ele nao consegue criar topicos
(`not enough rights to create a topic`), apenas postar nos que ja existem.

Testado ao vivo: `sendMessage` no thread 2 retornou `is_topic_message: true`,
`message_thread_id: 2`. Mensagem de confirmacao deixada no topico para o usuario ver.

### Erros meus no caminho

- `patch` trocou `reuniao` por `reunion` (espanhol) - corrigido na sequencia
- `patch` reindentou o bloco final do `hermes-automation-ideas.py` (IndentationError) -
  corrigido e `py_compile` passou
- **conclusao errada minha:** antes de sondar, afirmei que o bot *nao enxergava nenhum topico*.
  Ele nao enxergava os que eu testei (4348330719, 1, 3-12); o certo era 2, e funcionava.
  Eu tinha usado o id do grupo como se fosse o id do topico.

---
## 2026-10-01 (fim de dia 5) - varredura final de lixo

- Varrido o `Hermes/` inteiro em busca de backup, temporario, duplicata e pasta orfa.

### Removido

| Caminho | MB | Porquê |
|---|---|---|
| `_mvtest/` | 0 | Pasta `x` vazia criada as 16:30 de hoje por um teste meu de movimento. Lixo meu. |
| `LinkedIn-backup-pre-cleanup.tar.gz` | 36,83 | Snapshot anterior a limpeza. O repo `Linkedin/` esta integro (commit `940079a` de 2026-10-01 14:20, working tree limpa, remote `linkedin-automation`). SHA-256 registrado em `_archive/apagado-linkedin-backup-2026-10-01.json`. |

### Documentado (nao era lixo)

- `hermes-config-repo/` (522 MB) **nao estava no README raiz** - corrigido. E o backup
  ativo de config, escrito pelo job das 06:00 na branch `auto-sync`. O README agora avisa
  que o `.gitignore` dele exclui `.env`, `auth.json`, `state.db`, `memories/` e `cron/`,
  portanto NAO e um backup completo do install.

### Avaliado e mantido

- `models/gguf/` — 16,59 GB de pesos. Legitimo.
- `Linkedin/.venv/` (52,14 MB) + `.pytest_cache/` — regeneravel, mas economiza reinstall.
  Decisao deixada para o usuario.
- `skills-repos/` 179 MB de repos clonados — e a pasta de referencia por definicao.

### Pendencias inertes

- `Hermes/nul` e `Hermes/_trash/nul` — device name reservado do Windows; `os.rename`,
  `shutil.move` e `unlink` falham com WinError 5. Remocao exige prompt admin:
  `del \\?\C:\Users\gsalo\Hermes\nul`

---
## 2026-10-01 (fim de dia 4) - _archive limpa

- **310,75 MB apagados.** `_archive/` nao tem mais nenhum item ativo.

### Removido

| Item | MB | Porquê |
|---|---|---|
| `hermes-backup-antes-perfis.zip` | 308,25 | Continha a senha do Gmail em texto puro. Era a ultima copia dessa credencial no disco. |
| `teste-limpo-export.tar.gz` | 2,43 | Perfil de teste ja deletado. |
| `hermes-agent-knowledge/` | 0,05 | Repo clonado, 10 ficheiros placeholder de ~1 KB, sem conteudo. |
| ficheiros soltos de 17-29/09 | 0,02 | `gerar_logo*.py`, `nous_*.json`, `todoist-*.json`, `gpu_type.txt`, etc. Sem referencia. |

### Preservado (~138 KB)

- Os 8 manifests de integridade + `state-db-audit.json` — unica prova de que as
  movidas de hoje nao perderam nada.
- `apagado-2026-10-01-manifest.json` (novo) — SHA-256 de cada ficheiro removido.
- `_organize_log.json`, `hermes-config-sync.py.removido`, `job-removido-*.json`.

### Verificacao

- Varredura por path absoluto `C:\\Users\\gsalo\\Hermes\\_archive` em `scripts/`,
  `profiles/`, `skills/`, `cron/`, `config.yaml` e `memories/`: **0 achados**. As 39
  ocorrencias da palavra `archive` sao codigo generico (`create_vetted_tar_archive`,
  `try_archive_today`) ou prosa de skill a explicar a convencao.
- Normalizacao de atributos necessaria antes do `rmtree`: 89 ficheiros (o `.git` da
  `hermes-agent-knowledge` tinha READ-ONLY, igual ao `hermes-config-backup` de antes).

### Consequencia aceita

Nao resta nenhum backup com a config **completa**: o `hermes-config-repo/` cobre
config, mas o `.gitignore` dele exclui `memories/`, `cron/` e `state.db`. Decisao do
utilizador, ja registada.

---
## 2026-10-01 (fim de dia 3) - job hermes-config-sync removido

- **Job `hermes-config-sync` (03:00) apagado** de `cron/jobs.json`. Estava parado desde
  25/09: ultimo commit em 24-25/09, `sync.log` nunca existiu (so e escrito quando ha mudanca).
- **Pasta `_archive/hermes-config-backup/` removida** (1,25 MB, 357 arquivos, 2 commits).
  O snapshot de 25/09 foi descartado por decisao explicita do usuario.
- **Script `scripts/hermes-config-sync.py` removido** (copia em
  `_archive/hermes-config-sync.py.removido`).
- **Substituido por:** `sync_diario.sh` das 06:00 -> `Hermes/hermes-config-repo/`, que usa
  branch `auto-sync`, nao empurra segredos (`.gitignore` bloqueia `.env`/`auth.json`) e roda
  com auto-sync funcional (ultimo commit 2026-10-01 16:32).

### Detalhe tecnico

- `shutil.rmtree` falhou com `WinError 5` em `.git/objects/`: 209 arquivos com atributo
  READ-ONLY (comum em repos git). Resolvido com `os.chmod(S_IWRITE)` em todos os arquivos
  antes de remover. Verificar e normalizar atributos ANTES de `rmtree` em arvores git.
- Antes de apagar: repo com working tree limpa, zero commits nao pushados, e os 23
  arquivos exclusivos dela (configs dos perfis, `cron/jobs.json`, `memories/*.md`) nao
  existiam no repo sucessor - decisao do usuario: perder esse snapshot e aceitavel.
- Skill `devops/telegram-cron-setup/SKILL.md` atualizada (tabela de jobs + File Locations),
  para nao documentar um job que nao existe mais.

### Estado do agendamento: 7 jobs

- Global (3): Morning briefing 08:00, automation-ideas 08:00, Model Routing Score Update 09:00
- research-senior (4): AI News Briefing V3 07:05, Suno Newsletter Agent 08:05,
  Hermes Desktop Daily Curation 09:00, Backup Hermes Config 06:00

---
## 2026-10-01 (fim de dia 2) - _trash esvaziada

- `_trash/` purgada: **191,43 MB removidos**, 420 ficheiros.
  - `nested-profiles-scripts-20261001/` (187,89 MB, 93 arq)
  - `nested-skills-research-senior-20261001/` (3,53 MB, 327 arq)
- Pre-condicoes verificadas: zero ficheiros escritos nas copias depois da auditoria
  (nada novo desde 16:13 e 12:46); remocao confirmada por ausencia dos caminhos.
- **Beneficio de seguranca:** desapareceram 3 copias de `auth.json` (~13 KB, 20 chaves
  sensiveis cada) que estavam esquecidas em diretorios nao resolvidos.
- `_trash/README.md` reescrito com o historico do que passou por la e porquê.

### _archive NAO foi apagada (decisao do utilizador adiada)

- `hermes-config-backup/` (1,25 MB) e **destino do job `hermes-config-sync` das 03:00**.
  Apagar faria esse job falhar - o mesmo modo de falha do `Path.home()` anterior.
- Ainda candidatos (nao tocados): `hermes-backup-antes-perfis.zip` (308,25 MB, contem a
  senha do Gmail em texto puro), `teste-limpo-export.tar.gz` (2,43 MB), e ficheiros soltos
  de 17-29/09. Os 8 manifests de integridade (~1 KB cada) devem ser mantidos.

---
## 2026-10-01 (fim de dia) - pendencias abertas registradas

Sessao encerrada com tudo verificado e estavel. Duas pendencias NAO tocadas
nesta sessao, apenas registradas:

### 1. `hermes-config-repo/` (207 MB) ainda fora do Hermes

- Caminho: `C:\Users\gsalo\hermes-config-repo` (raiz do usuario).
- E repo git, branch `auto-sync`, funcinando (rodou 16:14, "no changes").
- `sync_diario.sh` (o que o cron das 06:00 usa) tem `ROOT="/c/Users/gsalo/hermes-config-repo"`.
- Para mover: actualizar `ROOT` no script + mover com SHA-256 + verificar proximo sync.

### 2. Copia quebrada de `sync_diario.sh` dentro de uma skill

- `profiles/research-senior/skills/devops/config-repo-backup/scripts/sync_diario.sh`
  tem placeholders NAO preenchidos: `ROOT="/absolute/path/to/backup-clone"`,
  `L="/absolute/path/to/live/install"`, `REMOTE_URL="https://github.com/<owner>/<repo>"`.
- Faz `exit 1` na linha 19. A versao boa e `profiles/research-senior/scripts/sync_diario.sh`.
- Risco: a skill e partilhada; outro agente pode usar a copia quebrada.

### Estado final verificado

- Gateway `running`, Telegram `connected`, 8 cron jobs (4 global + 4 research-senior).
- Raiz `C:\Users\gsalo`: nenhum ficheiro solto do Hermes (pasta `hermes-config-repo`(exceto esta)).
- Todos os dados dos perfis abrem: 25 tabelas, 18.381 / 11.933 / 12.357 mensagens.
- `WIKI_PATH` aponta para `Hermes/wiki`; pipeline de email validado com envio real.

### Pendencias do utilizador

- Trocar a senha do Gmail (esteve em texto puro; segue no backup de 323 MB e nos `.bak`).
- Depois actualizar `SMTP_APP_PASSWORD` e `SUNO_LOGIN_PW` no `.env` do research-senior.
- Confirmar entrega do briefing das 07:05 (primeira prova com agendamento real).

### Pendencias inertes

- Lock orfao de 0 byte (sai fechando o Hermes Desktop).
- 2 ficheiros `nul` (precisam de prompt admin: `del \\?\C:\Users\gsalo\Hermes\nul`).
- `auth.json` duplicados preservados em `_trash/` — revisao manual antes de esvaziar.

---
## 2026-10-01 (tarde 5) - 188 MB de perfis duplicados removidos

- `profiles/research-senior/scripts/profiles/<perfil>/` (93 arquivos, 187,89 MB) movida
  para `_trash/nested-profiles-scripts-20261001/`. **93/93 SHA-256 conferidos, 0 falhas.**
- **Mesmo bug do curador** que recursa sobre si mesmo, agora em `scripts/` e nos outros
  dois perfis. Continha `state.db` (158 MB) + `auth.json` (~13 KB, 20 chaves sensiveis) de
  cada perfil duplicados.
- **Auditoria antes de remover:** os `state.db` reais sao sempre mais novos (esta sessao
  escreve no do research-senior em tempo real). Aninhados = fotografia parada de 15:05.
  Estruturalmente o aninhado esta 2 niveis abaixo de `profiles/`, e a resolucao de perfis
  so enxerga filhos diretos - nenhum perfil pode ser resolvido ali.
- **Verificacao pos-move:** 25 entradas em `scripts/`, `env_loader.py` e
  `ai_news_briefing.py` intactos; os 3 `state.db` reais abrem com 25 tabelas e 18.381 /
  11.933 / 12.357 mensagens; os 3 `auth.json` reais com 20 chaves sensiveis cada.
- Manifest: `_archive/nested-profiles-scripts-manifest.json`.

### Pendencia de seguranca que sobrou

Os `auth.json` duplicados estao agora em `_trash/`, nao removidos. Sao credenciais reais
(tokens de API dos perfis) multiplicadas em 3 diretorios esquecidos. **Nenhum `.env` foi
copiado** - as senhas SMTP/Suno nao estao ali. Revisao manual recomendada antes de
apagar o `_trash`.

---
## 2026-10-01 (tarde 4) — wiki movida para dentro do Hermes

- `~/wiki` (vault Obsidian, 6 arquivos, 5.232 B) movida para `Hermes/wiki/` — 6/6 SHA-256 conferidos; manifest em `_archive/wiki-manifest-pre-move.json`.
- **Nao foi para `skills-repos/`:** aquele diretorio e so referencia (o README avisa que o Hermes nao carrega skills dali) e contem apenas repos git clonados. A wiki e conteudo, nao repo.
- **Configurado:** `WIKI_PATH=C:/Users/gsalo/Hermes/wiki` no `.env` global (18 -> 19 chaves, nenhuma perdida; backup `.env.bak-antes-wikipath`). A skill `research/llm-wiki` usa essa variavel com fallback `~/wiki`; agora o caminho e explicito e sobrevive a proxima limpeza da raiz.
- **Estado:** vault vazio — `index.md` com `Total pages: 0`, 6 pastas de conteudo vazias, `log.md` so com o registro de criacao de 24/09, e `llm-wiki` com `use_count: 0`. Nada por cron/script/config. Mover era seguro.
- **Corrigido em `wiki/README.md`:** caminho do vault no Obsidian + secao de estado atual.


## 2026-10-01 (tarde 3) — arvore de skills duplicada removida do research-senior

- `profiles/research-senior/skills/profiles/research-senior/skills/` (326 arquivos, 3,5 MB) foi movida para `_trash/nested-skills-research-senior-20261001/`.
- **Causa:** o curador automatico recriou as proprias skills dentro de si mesmo as 12:46 de hoje.
- **Auditoria antes de remover:** 323 de 326 byte-identicos; os 3 divergentes (`ai-news-briefing/SKILL.md`, `.curator_ledger.jsonl`, `.usage.json`) tem a versao REAL mais nova (14:00 vs 12:46). Zero arquivos exclusivos da arvore aninhada. Nada em codigo/config/cron a invoca.
- **Impacto:** `get_all_skills_dirs()` nao a resolvia (so 2 diretorios), mas `rglob` recursivo em `learning_graph.py` e `curator_backup.py` sim — inflava as metricas com copias.
- **Verificacao pos-move:** 327/327 SHA-256 conferidos, origem removida, 69 `SKILL.md` reais intactos, arvore ausente da resolucao.
- Manifestos: `_archive/nested-skills-audit.json`, `_archive/nested-skills-manifest-pre-trash.json`, `_archive/nested-skills-recheck.json`.
- **Nao e aninhamento:** `skills/research-senior/promo-claim-vetting/` — e a categoria de skill criada pelo curador (padrao `skills/<categoria>/<nome>/`). Mantido.


## 2026-10-01 (tarde 2) — raiz do usuario 100% limpa

- Movidos para `Hermes/data/`: `nous-scout-results.json` e `AI_News_Briefing.html` (2/2 SHA-256 conferidos; manifest em `_archive/manifest-pre-move-root-files.json`).
- **3 linhas de codigo repontadas** (com backup em `profiles/research-senior/backups/config/`): `scripts/nous-scout.py:23`, `profiles/research-senior/scripts/generate_briefing.py:11`, `profiles/research-senior/scripts/run_send.py:8`.
- **3 referencias em prosa atualizadas** na mesma passada: `scripts/add-scout-cron.py:23`, `skills/hermes-configuration/SKILL.md:395`, `profiles/research-senior/skills/productivity/ai-news-briefing/SKILL.md:37`.
- **Validado com execucao real** sob o interpretador bundled do cron: `generate_briefing.py` (exit 0, 8 noticias) -> `run_send.py` (**email enviado**, exit 0).
- **Armadilha encontrada:** o runtime Python do Hermes foi atualizado para `cpython-3.11.16-windows-x86_64-none`; o path `cpython-311-windows-x86_64-none` que eu tinha anotado **nao existe mais** (`WinError 2`). Resolva o interpretador dinamicamente (`glob` em `.hermes-runtime/python/*/python.exe`) em vez de fixar versao em codigo.
- `briefing_output.json` tambem saiu da raiz: ja vivia corretamente em `profiles/research-senior/data/` (o gerador e o job leem de la).
- **A raiz `C:\Users\gsalo` nao tem mais nenhum arquivo solto do Hermes.** O que sobrou sao dotfiles de shell, `NTUSER*`, `config.yaml` de outro projeto e pastas nao-Hermes (`ComfyUI/`, `OmniRoute/`, `env/`, `models/`, `wiki/`, `workspace/`).

## 2026-10-01 (tarde) — pipeline de briefing testado ponta a ponta

- **Bug encontrado e corrigido (culpa minha):** `send_email.py`, `send_briefing.py` e `send_newsletter.py` importavam `python-dotenv`, que **nao existe** no interpretador bundled do Hermes (o que o cron usa). Eu tinha "testado" esses scripts antes com um interpretador que tinha o pacote — o teste nao era valido. O job das 07:05 ia falhar calado.
- **Correcao:** criado `profiles/research-senior/scripts/env_loader.py` (stdlib only, sem dependencia). Backups: `profiles/research-senior/backups/config/*.2026101-pre-dotenv-fix.bak`.
- **Pipeline validado com execucao real:** `ai_news_briefing.py` coletou 13 artigos -> `generate_briefing.py` gerou HTML com 8 noticias (7.685 B, 21/22 checks de layout) -> `run_send.py` **enviou o email** (`exit 0`).
- **Corrigido registro anterior:** `briefing_output.json` NAO estava ausente — existe em `profiles/research-senior/data/` (89 B) e era consumido corretamente. O defeito real era o dotenv.
- Pendente: mover `nous-scout-results.json` e `AI_News_Briefing.html` da raiz para `Hermes\` (exige ajustar 3 linhas: `nous-scout.py:23`, `generate_briefing.py:11`, `run_send.py:8`).

## 2026-10-01 — other profiles active again, creds out of scripts

**Gateway multiplexing fixed.** The 4 Telegram bots had gone silent: valid bot
tokens, but no process polling them. Cause was inconsistent config —
`multiplex_profiles: false` in the global `config.yaml` while each profile's own
config said `true`, so the single gateway served `served_profiles: []`. Set to
`true` and restarted; all four reconnected at 18:11 and `served_profiles` now
lists all 4. The cron scheduler also began ticking 5 profiles instead of 1, which
reactivated 3 dormant `research-senior` jobs.

**`teste-limpo` profile deleted.** It was a throwaway test profile. Exported to
`_archive/teste-limpo-export.tar.gz` (2.4 MB, 272 entries) first. The CLI
removed `config.yaml`/`.env` and dropped it from `profile list`, but failed on a
`logs/.__agent.lock` handle, leaving 94 files behind; 93 were removed later and
the alias `~/.local/bin/teste-limpo.bat` was deleted. One 0-byte lock file
remains, held by the Hermes Desktop `serve --profile default` process (PID
changes) — harmless, clears when Desktop closes. The CLI also writes a
tombstone at `profiles/.deleted/teste-limpo`; that is intentional.

Removing this profile also resolved a collision: its `nous-scout.py` wrote to
the same `C:\Users\gsalo\nous-scout-results.json` as the global one.

**Credentials moved out of source.** `send_email.py`, `send_briefing.py`,
`suno_newsletter.py` had a Gmail app password hardcoded; `suno_newsletter.py`
also had the account login password for AWS Cognito. All now read from
`profiles/research-senior/.env` (`SMTP_*`, `SUNO_*`). Verified by import —
values load, and no literal password remains in any active script. Backups of the
old versions sit in `profiles/research-senior/backups/config/`.

> The Gmail **login password was exposed** before this change and is still inside
> the backup zip below. Rotating that password is still outstanding.

**`platforms.email` disabled.** It was enabled with no credentials, so every boot
logged ~33 adapter-creation failures across 4 profiles. Disabled in the global
config; the platform is for *reading* mail and was never configured. Outgoing
briefings are unaffected — they use `smtplib` directly in the scripts above.

**`MEMORY.md` trimmed** from 2,266 → 1,896 chars (limit 2,200). Removed two
task-log entries another profile had written (a rendered video path, a job-search
goals line — both files still exist) and fixed a stale `skills-repos` path that
still pointed at the pre-move location.

## 2026-10-01 (later) — cron job broken by the reorg, found and fixed

**`hermes-config-sync` was failing because of the 09-30 move.** The script resolves
its repo as `Path.home() / "hermes-config-backup"`; that folder moved to
`_archive/hermes-config-backup`, so the 03:00 run exited with code 1. Repointed to
the absolute path and verified by running it (exit 0). Backup alongside the script
as `.bak-antes-path-fix`.

**Lesson:** moving a folder is only safe if every *script* that resolves it
dynamically is re-checked. The 09-30 dependency scan covered hardcoded paths in
config/skills but not `Path.home() / "<name>"` patterns in cron scripts. Scanned
all cron scripts for that pattern — the other two (`hermes-morning-briefing.py`,
`hermes-automation-ideas.py`) target `~/.hermes`, untouched by the move, so they
are fine.

**`platforms.email` disabled in the three named profiles too.** It had only been
turned off in the global config, but each profile carries its own block, so the
adapter would still be attempted per profile under multiplexing. All five configs
now agree.

## 2026-10-01 (end of day) — lessons written down

Consolidated today's work into skills so the next session does not rediscover it:

- **`devops/hermes-gateway-triage`** (new) — silent-bot diagnosis: prove the token is
  actually valid before blaming it, read `served_profiles` and per-profile platform
  state, understand multiplex vs per-profile gateways, the two distinct profile
  pointers, and that `profile delete` unroutes while leaving files behind.
- **`devops/local-secret-hygiene`** (new) — moving a literal credential into `.env`:
  extract rather than retype, build redacted key names by concatenation, verify with a
  real import, and the point that relocating a secret is not revocation.
- **`devops/windows-file-reorg-safety`** (updated) — dynamic path resolution
  (`Path.home()`) defeats a hardcoded-path dependency scan; the redaction pitfall that
  corrupted scripts twice.

Fixed a structural bug in that last skill: a patch had eaten a section heading, leaving
orphaned prose under the wrong heading.

**Memory maintenance.** `MEMORY.md` had a trailing `§` that made the file unparseable
for the memory tool (it refused three writes as "drift" while the bytes were provably
identical). Normalised to a clean `§`-delimited list. Removed two stale `.bak` files
from `memories/` that were themselves causing version drift.

## 2026-09-30 — repo reorganised

**User profile root cleaned:** 130 → 17 loose files. 113 files and 11 folders
moved into themed folders here; every file SHA-256 checked before and after
(0 mismatches). Three files were left in place because live code hardcodes their
paths: `nous-scout-results.json`, `AI_News_Briefing.html`, and `briefing_output.json`.

**`hyperframes/` moved to `Videos/hyperframes/`.** Manifest of all 214 files
(size + SHA-256) recorded in `_archive/hyperframes-manifest-pre-move.json`;
re-verified 214/214 after the move. The one live reference
(`media-generation/references/video-project-workspace.md`) was updated.

**README tree created.** This file's parent `README.md` indexes every folder;
12 project areas have their own `README.md`, plus `SUPPORT.md` for the working
folders.

**Backup:** `hermes-backup-antes-perfis.zip` (323 MB, 6,231 entries) with a
tested restore path (`hermes import`). Contains credentials — see above.

## Known leftovers

- `Hermes/nul` and `Hermes/_trash/nul_Hermes` — Windows reserved device name;
  only removable from an admin prompt via `del \\?\C:\Users\gsalo\Hermes\nul`
- `profiles/teste-limpo/logs/.__agent.lock` — see 2026-10-01 entry
- WhatsApp unpaired on the default profile; disabled on the other three under
  multiplexing (shared ingress is per-process)

---
## 2026-10-08 — content-repurpose project created (ranking #4)

### Projeto novo: content-repurpose\
\
- Pasta: `content-repurpose/` (raiz do Hermes)\
- Pipeline: texto → vídeo curto (reels/TikTok/shorts) com narração PT-BR\
- Stack: HyperFrames + edge_tts / Qwen3-TTS-AMD + FFmpeg\
- Receita alvo: R$500–1.5K/mês (4–8 vídeos) ou R$120/vídeo\
- Status: setup inicial — README + meta.json criados\
- Documentado em CHANGELOG.md e README.md do projeto
