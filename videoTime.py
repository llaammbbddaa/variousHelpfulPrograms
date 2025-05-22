import os
import subprocess
from datetime import timedelta

# Supported video file extensions
VIDEO_EXTENSIONS = {'.mp4', '.mkv', '.avi', '.mov', '.flv', '.webm'}

def is_video_file(filename):
    return any(filename.lower().endswith(ext) for ext in VIDEO_EXTENSIONS)

def get_video_duration(file_path):
    try:
        result = subprocess.run(
            [
                'ffprobe', '-v', 'error',
                '-show_entries', 'format=duration',
                '-of', 'default=noprint_wrappers=1:nokey=1',
                file_path
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return float(result.stdout.strip())
    except Exception:
        return 0.0

def get_total_video_duration(directory):
    total_seconds = 0.0
    for root, _, files in os.walk(directory):
        for file in files:
            if is_video_file(file):
                file_path = os.path.join(root, file)
                duration = get_video_duration(file_path)
                total_seconds += duration
    return timedelta(seconds=int(total_seconds))

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ").strip()
    if os.path.isdir(folder_path):
        total_duration = get_total_video_duration(folder_path)
        print(f"\nTotal video duration in '{folder_path}': {total_duration}")
    else:
        print("Invalid folder path.")
