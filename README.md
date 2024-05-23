# motivation-scraper
This script uses speech-to-text and language models to convert videos from motivational speakers into simple, easy to digest quotes.

Essentially, my script scrapes the video, extracts the audio, transcribes it, then generates quotes by utilizing the ideas discussed, thereby extracting the most valuable moments into text form. 

I created this because often times these speakers will talk too fast, leaving listeners unable to truly absorb what is being said, plus text can be re-read later too, without listening to the video again. Ultimately my tool allows to you better absorb and retain valuable information. 

![screenshot of example usage](assets/screenshot.png)

## Installation
- `pip install -r requirements` (virtual environment recommended)
- You'll also need to set up a `.env` file with an OpenAI key, with access to "whisper-1" and "gpt-3.5-turbo" enabled. See `.env.example` for more info

## Usage
- `python main.py <url>`
- For now, YouTube and Instagram are the only supported video platforms. 

## License
MIT
