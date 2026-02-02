#!/usr/bin/env python3
"""
Generate Music with Lyria
"""
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from ai_content.core.registry import ProviderRegistry
from ai_content.presets.music import get_preset as get_music_preset
import ai_content.providers  # noqa: F401

async def generate_music(style: str = "jazz"):
    print(f"🎵 Generating {style} music...")

    preset = get_music_preset(style)
    if not preset:
        print(f"❌ Unknown style: {style}")
        return

    provider = ProviderRegistry.get_music("lyria")
    result = await provider.generate(
        prompt=preset.prompt,
        bpm=preset.bpm,
        duration_seconds=10,
    )

    if result.success:
        print(f"✅ Music saved at: {result.file_path}")
    else:
        print(f"❌ Failed: {result.error}")

if __name__ == "__main__":
    style = sys.argv[1] if len(sys.argv) > 1 else "jazz"
    asyncio.run(generate_music(style))
