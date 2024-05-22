import random
import string
import subprocess


def generate_random_string(length: int) -> str:
  return "".join(random.choices(string.ascii_lowercase, k=length))


def extract_audio(video_file_path: str) -> str:
  audio_file_path = f"audio/audio_{generate_random_string(16)}.wav"

  try:
    # extract audio from video
    result = subprocess.call(
      ["ffmpeg", "-i", video_file_path, "-vn", "-ar", "44100", "-ac", "2", "-ab", "192k", "-f", "wav", audio_file_path],
      stdout=subprocess.DEVNULL,
      stderr=subprocess.DEVNULL,
    )
    
    if result != 0:
      raise Exception("Failed to extract audio from video")

    print(f"Audio extracted successfully and saved to {audio_file_path}")
  except Exception as e:
    print(f"An error occurred: {e}")

  return audio_file_path
