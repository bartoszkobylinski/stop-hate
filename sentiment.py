import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')
engine = os.getenv('OPENAI_ENGINE', 'text-davinci-003')
prompt_template = os.getenv('OPENAI_SENTIMENT_PROMPT')
def analyze_sentiment(comment):
    response = openai.Completion.create(
      engine=engine,
      prompt=prompt_template,
      temperature=0.5,
      max_tokens=60,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    return response.choices[0].text.strip()
