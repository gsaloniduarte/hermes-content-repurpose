# Content Repurpose — Projeto HyperFrames

Pipeline de texto → vídeo curto (reels/TikTok/shorts) com narração PT-BR.

## Estrutura
- `index.html` — Ponto de entrada da composição HyperFrames
- `compositions/` — Templates de cena
- `scripts/pipeline.py` — Pipeline de automação
- `renders/` — Output final
- `images/` — Galeria compartilhada

## Pipeline
1. Captura frames de URL (Playwright)
2. Gera narração PT-BR (edge_tts)
3. Compõe com HyperFrames (GSAP animações)
4. Mistura áudio (BGM + SFX + voz)
5. Renderiza para MP4
6. Publica na galeria

## Stack
- HyperFrames @0.8.77
- GSAP 3.14.2
- edge_tts / Qwen3-TTS-AMD
- FFmpeg
- Playwright

## Regras
1. Verificar LICENSE de imagens antes de usar
2. Render com timeout; matar node.exe zombie antes de rm
3. Atualizar CHANGELOG.md a cada iteração
4. Sempre run `npm run check` antes de render
5. Documentar mudanças no CHANGELOG.md

## Status
2026-10-08: projeto criado, pipeline ativo, aguardando primeiro conteúdo fonte
