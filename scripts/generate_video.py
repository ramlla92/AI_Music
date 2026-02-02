#!/usr/bin/env python3
"""
Generate Video with Veo
"""
import asyncio
import sys
from pathlib import Path

from google.genai.types import GenerateVideosConfig

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from ai_content.core.registry import ProviderRegistry
from ai_content.presets.video import get_preset as get_video_preset
import ai_content.providers  # noqa: F401


async def generate_video(style: str = "nature"):
    print(f"🎬 Generating {style} video...")

    preset = get_video_preset(style)
    if not preset:
        print(f"❌ Unknown style: {style}")
        return

    provider = ProviderRegistry.get_video("veo")

    # ⚠️ Config = video params ONLY
    config = GenerateVideosConfig(
        aspect_ratio=preset.aspect_ratio,
        duration_seconds=5,
    )

    # ✅ Prompt passed directly
    result = await provider.generate(
        prompt=preset.prompt,
        config=config,
    )

    if result.success:
        print(f"✅ Video saved at: {result.file_path}")
    else:
        print(f"❌ Failed: {result.error}")


if __name__ == "__main__":
    style = sys.argv[1] if len(sys.argv) > 1 else "nature"
    asyncio.run(generate_video(style))
