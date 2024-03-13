import openai
import os

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
