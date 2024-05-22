import dotenv
dotenv.load_dotenv()

import openai
import diskcache


transcribe_audio_cache = diskcache.Cache("cache/transcribe_audio")


@transcribe_audio_cache.memoize()
def transcribe_audio(audio_file_path: str) -> str:
  with open(audio_file_path, "rb") as audio_file:
    transcription = openai.audio.transcriptions.create(
      model="whisper-1", 
      file=audio_file,
    )
  return transcription.text
