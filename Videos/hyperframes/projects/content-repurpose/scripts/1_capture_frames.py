#!/usr/bin/env python3
"""Script 1: capture_frames — captura frames de uma URL."""
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
IMAGES_DIR = BASE_DIR / "images" / "frames"
CONFIG = {
    "format": "reels",
    "resolution": {"width": 1080, "height": 1920},
    "fps": 30
}

def ensure_dirs():
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

def log(msg):
    print(f"[capture_frames] {msg}", flush=True)

def run(cmd, check=True):
    log(f"→ {cmd}")
    result = os.system(cmd)
    if check and result != 0:
        log(f"❌ Erro: {result}")
        sys.exit(1)
    return result

def capture_frames(url, output_dir, num_frames=6):
    log(f"📸 Capturando {num_frames} frames de {url}")
    run(f"npx playwright --url '{url}' --frames {num_frames} -o '{output_dir}'")
    return output_dir

def main():
    log("🚀 Iniciando capture_frames")
    ensure_dirs()
    import argparse
    parser = argparse.ArgumentParser(description="Capture frames from URL")
    parser.add_argument("url", help="URL to capture")
    parser.add_argument("--frames", type=int, default=6, help="Number of frames")
    args = parser.parse_args()
    capture_frames(args.url, IMAGES_DIR, args.frames)
    log("✅ Captura concluída")

if __name__ == "__main__":
    main()
