from prompt_settings import settings
import openai
import os

system_api_key = os.getenv("SYSTEM_API_KEY")
user_apki_key = os.getenv("USER_API_KEY")


def request_open_ai(prompt, api_key, sys_prompt, settings):
    openai.api_key = api_key
    completion = openai.ChatCompletion.create(
        model=settings.model,
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": prompt}
        ],
        max_tokens=settings.max_token,
        n=settings.n,
        temperature=settings.temperature
    )


