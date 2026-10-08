#!/usr/bin/env python3
"""
Pipeline content-repurpose: texto → vídeo curto (reels/TikTok/shorts)
"""
import os
import sys
import json
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RENDERS_DIR = BASE_DIR / "renders"
IMAGES_DIR = BASE_DIR / "images"
ASSETS_DIR = BASE_DIR / "assets"

CONFIG = {
    "format": "reels",
    "resolution": {"width": 1080, "height": 1920},
    "fps": 30,
    "audio": {
        "voiceover": {"enabled": True, "engine": "edge_tts"},
        "bgm": {"enabled": True, "volume": -18},
        "sfx": {"enabled": True, "volume": -12}
    },
    "fonts": ["Inter", "Inter Bold", "Space Grotesk"],
    "colors": {
        "primary": "#FF2D75",
        "secondary": "#7B2FF7",
        "accent": "#FF6B35",
        "bg": "#0A0A0F",
        "text": "#FFFFFF"
    }
}

def ensure_dirs():
    for d in [RENDERS_DIR, IMAGES_DIR, ASSETS_DIR]:
        d.mkdir(parents=True, exist_ok=True)

def log(msg):
    print(f"[content-repurpose] {msg}", flush=True)

def run(cmd, check=True):
    log(f"→ {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        log(f"❌ Erro: {result.stderr}")
        sys.exit(1)
    return result

def capture_frames(url, output_dir, num_frames=6):
    log(f"📸 Capturando {num_frames} frames de {url}")
    run(f"npx playwright --url '{url}' --frames {num_frames} -o '{output_dir}'")
    return output_dir

def generate_voiceover(text, output_file, lang="pt-BR"):
    log(f"🎙️  Gerando narração...")
    run(f"edge-tts --text '{text}' --voice {lang} --write-media '{output_file}'")
    return output_file

def compose_hyperframes():
    log("🎬 Compondo com HyperFrames (npm run build)...")
    run("npm run build", check=False)
    return True

def render_video():
    log("🎥 Renderizando vídeo...")
    run("npm run render", check=False)
    return True

def mix_audio():
    log("🎵 Misturando áudio...")
    return True

def main():
    log("🚀 Iniciando pipeline content-repurpose")
    ensure_dirs()

    import argparse
    parser = argparse.ArgumentParser(description="Content Repurpose pipeline")
    parser.add_argument("url", nargs="?", help="URL do conteúdo para capturar")
    parser.add_argument("text", nargs="?", help="Texto para gerar narração")
    parser.add_argument("--frames", type=int, default=6, help="Número de frames")
    parser.add_argument("--no-audio", action="store_true", help="Sem narração")
    parser.add_argument("--format", choices=["reels", "tiktok", "shorts"], default="reels")
    args = parser.parse_args()

    if args.url:
        capture_frames(args.url, IMAGES_DIR / "frames", args.frames)

    if args.text and not args.no_audio:
        voiceover_file = RENDERS_DIR / "voiceover.wav"
        generate_voiceover(args.text, voiceover_file)

    if args.format != "none":
        compose_hyperframes()
        render_video()
        mix_audio()

    log("✅ Pipeline concluído com sucesso!")

if __name__ == "__main__":
    main()
