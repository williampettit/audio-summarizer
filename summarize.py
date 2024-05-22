import dotenv
dotenv.load_dotenv()

import openai
import diskcache


generate_bullet_points_cache = diskcache.Cache("cache/generate_bullet_points")


@generate_bullet_points_cache.memoize()
def summarize_transcription(text: str) -> str:
  response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": """
          You will be given an audio transcription from a short motivational video, likely talking about how to be successful in all walks of life.
          Your task is to summarize the transcription into motivational quotes.

          You should take into consideration the following preferences when generating quotes:
          - Do not assume the reader of the quotes has any prior knowledge of the video
          - Write each quote as a complete sentence at minimum, and treat each quote independently
          - If the transcription mentioned a specific life example, you could include that in the quote to make it more relatable
          - The overall tone of the quotes should be positive, uplifting, and most importantly, easy to understand
          - Each quote should be a bullet point
          - You can use the same words as in the transcription, but you should not copy the text verbatim
          - You can use markdown to format the text

          Essentially, you are creating a list of motivational quotes, by using ideas discussed in the transcription.
          Extract the most valuable moments from the video and convert them to text form.

          Let's begin. The transcription is as follows:
        """.strip(),
      },
      {
        "role": "user",
        "content": text.strip(),
      },
    ],
  )

  bullet_points = response.choices[0].message.content

  if not bullet_points:
    raise Exception("Bullet points not generated")

  return bullet_points

