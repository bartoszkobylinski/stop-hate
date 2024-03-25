from dotenv import load_dotenv
import os

load_dotenv()

main_prompt = os.getenv("MAIN_PROMPT")
hate_prompt = os.getenv("HATE_PROMPT")
valuable_prompt = os.getenv("VALUE_PROMPT")
user_prompt = os.getenv("USER_PROMPT")

