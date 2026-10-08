# Hermes — Projects Hub

Everything the Hermes agents create or modify for Gabriel lives here. Each
top-level folder is a **self-contained project area** with its own `README.md`.

> Rule for agents: when you create a new project, also create or update a
> `.md` in it. A folder with no `.md` is considered undocumented and unfinished.

## Project areas

| Folder | What it is |
|---|---|
|| `Videos/` | Video projects. `Videos/hyperframes/` holds the HyperFrames renders; one subfolder per project. |
|| `Imagens/` | Image generation: workflows (ComfyUI JSON), generated outputs, masks. |
|| `Audio/` | Voice-clone and TTS audio (Qwen3-TTS-AMD), including the audio README/changelog. |
|| `Musica/` | Music generation (ACE-Step), split by style. |
|| `Linkedin/` | LinkedIn automation: profile assets, job-hunting scripts, external references. |
|| `n8n-workflows/` | n8n automation workflows and media-tool specs. |
|| `models/` | Model files / metadata used by the agents. |
|| `wiki/` | LLM Wiki — an Obsidian vault for interlinked research notes. Driven by the `research/llm-wiki` skill via `WIKI_PATH`. Moved out of the user root on 2026-10-01. |
|| `hermes-config-repo/` | Git clone that backs up the Hermes config to `github.com/gsaloniduarte/hermes-config`. Written daily by the 06:00 `sync_diario.sh` job on the `auto-sync` branch. Its `.gitignore` excludes `.env`, `auth.json`, `state.db`, `memories/` and `cron/` — so it is **not** a full-install backup. Moved here from the user root on 2026-10-01. |
|| `content-repurpose/` | Video repurposing pipeline (text → reels/TikTok/shorts). PT-BR narration via edge_tts, composition via HyperFrames. **New 2026-10-08.** (raiz Hermes) |

## Support folders (not projects)

| Folder | Purpose |
|---|---|
| `scripts/` | Standalone one-shot Python scripts migrated from the user profile. |
| `data/` | Machine-generated output (briefing HTML, scout results). Nothing here is hand-edited. Moved out of the user root on 2026-10-01. |
| `logs/` | Old run/debug logs (`run_v*.log`, `step_*.png`). |
| `skills-repos/` | Cloned third-party skill repos (reference material, not loaded). |
| `_archive/` | Integrity manifests (SHA-256) from the 2026-10-01 moves, plus records of what was deleted. Nothing here is read at runtime. Purged 2026-10-01. |
| `_trash/` | Items pending review. Not deleted on sight — move here first, purge later. Empty as of 2026-10-01. |

## Rules

1. **One folder per project.** Don't create sibling folders with `-v2` / `-final`
   suffixes; iterate in place and keep history under `renders/` or similar.
2. **Document as you go.** Every new project folder gets a `README.md` describing
   what it is and how to regenerate it. **When you create or change something,
   update the relevant `.md` in the same task** — a folder whose docs describe
   the old layout is worse than no docs. Structural changes also get an entry in
   `CHANGELOG.md`.
3. **Update docs when you move things.** If you relocate a project, update every
   reference (skills, scripts, this file) in the same change.
4. **Archive, don't delete.** Move obsolete material to `_archive/` or `_trash/`
   rather than removing it.

See `SUPPORT.md` for what lives in the non-project folders
(`scripts/`, `logs/`, `skills-repos/`, `data/`, `_archive/`, `_trash/`).

## The user root is clean

As of 2026-10-01 there is **no loose Hermes file left in `C:\Users\gsalo`**.
Everything is either inside this hub or in `AppData\Local\hermes` (the active
install, which stays where it is by Gabriel's choice).

What remains in the root is not Hermes: shell dotfiles (`.bashrc`, `.gitconfig`),
Windows files (`NTUSER*`), a `config.yaml` belonging to an unrelated project,
and non-Hermes folders (`ComfyUI/`, `OmniRoute/`, `env/`, `models/`, `wiki/`,
`workspace/`). Do not move those.

## Integrity manifests

`_archive/` contains `*_manifest-*.json` files with the size + SHA-256 prefix of
every file, recorded before risky moves. Use them to verify nothing was lost.
