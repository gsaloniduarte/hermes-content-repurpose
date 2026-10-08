# Content Repurpose — Texto → Vídeo Curto

Progetto #4 do ranking automation-ideas (2026-10-08).

## O que faz
Transforma artigos/blogs/newsletters em reels, TikToks e shorts usando:
- Hermes + HyperFrames para composição
- Qwen3-TTS-AMD / edge_tts para narração PT-BR
- FFmpeg para render final
- BGM + SFX do bundle HyperFrames

## Receita alvo
R$500–1.500/mês (4–8 vídeos) ou R$120/vídeo

## Estrutura
- `compositions/` — templates HyperFrames
- `scripts/` — pipeline de extração, TTS, montagem
- `renders/` — output final
- `images/` — galeria compartilhada (stock + gallery-dl)

## Regras
- Verificar LICENSE de imagens antes de usar
- Render com timeout; matar node.exe zombie antes de rm
- Atualizar CHANGELOG.md a cada iteração

## Status
Setup: 2026-10-08 — aguardando primeiro conteúdo fonte

## GitHub
- Repo: `gsaloniduarte/hermes-content-repurpose`
- URL: https://github.com/gsaloniduarte/hermes-content-repurpose
- Branch padrão: master
- Push automático configurado
