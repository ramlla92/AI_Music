#!/usr/bin/env python3
"""
Combine Music and Video into a single video using FFmpeg
"""
import subprocess
import sys

# Paths to your generated files (update if needed)
music_file = sys.argv[1] if len(sys.argv) > 1 else "exports/lyria_20260202_131148.wav"
video_file = sys.argv[2] if len(sys.argv) > 2 else "exports/veo_nature_20260202_131148.mp4"
output_file = sys.argv[3] if len(sys.argv) > 3 else "exports/final_music_video.mp4"

print(f"🎵 Music: {music_file}")
print(f"🎬 Video: {video_file}")
print(f"📦 Output: {output_file}")

# Run ffmpeg command
subprocess.run([
    "ffmpeg",
    "-i", video_file,
    "-i", music_file,
    "-c:v", "copy",
    "-c:a", "aac",
    "-shortest",
    output_file
])

print("✅ Music video created!")
