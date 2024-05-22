import sys

from download import download_video
from summarize import summarize_transcription
from transcribe import transcribe_audio
from utils import extract_audio


def main() -> None:
  if len(sys.argv) > 1:
    page_url = sys.argv[1]
  else:
    page_url = input("Enter video URL: ")

  print("Downloading video")
  video_path = download_video(page_url)

  print("Extracting audio")
  audio_path = extract_audio(video_path)

  print("Transcribing audio")
  transcription = transcribe_audio(audio_path)

  print("Generating summary")
  summary = summarize_transcription(transcription)
  print(summary)


if __name__ == "__main__":
  main()
