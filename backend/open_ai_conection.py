import openai
import os

system_api_key = os.getenv("SYSTEM_API_KEY")
user_apki_key = os.getenv("USER_API_KEY")

def request_open_ai(prompt, api_key, sys_prompt):
    openai.api_key = api_key
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-tubro',
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1280,
        n=0.7,
        temperature=0.3
    )
