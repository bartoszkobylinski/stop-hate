from dotenv import load_dotenv
import os

load_dotenv()

main_prompt = os.getenv("MAIN_PROMPT")
hate_prompt = os.getenv("HATE_PROMPT")
valuable_prompt = os.getenv("VALUE_PROMPT")
user_prompt = os.getenv("USER_PROMPT")
twitter_prompt = os.getenv("TWITTER_PROMPT")
instagram_prompt = os.getenv("INSTAGRAM_PROMPT")
url_for_decisison = os.getenv("URL_PROMPT")

