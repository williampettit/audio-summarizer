import requests
import diskcache
import pytube

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from utils import generate_random_string


chrome_options = Options()
chrome_options.add_argument("--headless")

video_cache = diskcache.Cache("cache/video_cache")


def download_instagram_video(page_url: str) -> str:
  # initialize chrome driver
  service = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=service, options=chrome_options)
  
  try:
    # load page
    driver.get(page_url)
    
    # wait for video to load
    print("Waiting for video to load")
    driver.implicitly_wait(10)

    # wait for first video element to load
    video_element = WebDriverWait(driver, 30).until(
      EC.presence_of_element_located((By.TAG_NAME, "video"))
    )

    # extract src attribute
    video_src = video_element.get_attribute("src")

    if not video_src:
      raise Exception("Video src not found")
  finally:
    # close driver
    driver.quit()
  
  output_path = f"video/video_{generate_random_string(16)}.mp4"

  try:
    # get the video content
    response = requests.get(video_src, stream=True)
    response.raise_for_status()  # Check if the request was successful
    
    # open a local file with write-binary mode
    with open(output_path, "wb") as file:
      # stream video content and write to file in chunks
      for chunk in response.iter_content(chunk_size=8192):
        file.write(chunk)
            
    print(f"Video downloaded successfully and saved to {output_path}")
  except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

  return output_path


def download_youtube_video(page_url: str) -> str:
  video = pytube.YouTube(page_url).streams.get_lowest_resolution()

  if not video:
    raise Exception("Video src not found")
  
  output_path = f"video/video_{generate_random_string(16)}.mp4"

  return video.download(output_path=output_path)


@video_cache.memoize()
def download_video(page_url: str) -> str:
  if "youtube.com" in page_url:
    video_path = download_youtube_video(page_url)
  elif "instagram.com" in page_url:
    video_path = download_instagram_video(page_url)
  else:
    raise Exception("Unsupported video platform")

  return video_path
