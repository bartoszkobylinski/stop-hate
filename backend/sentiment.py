import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')
engine = os.getenv('OPENAI_ENGINE', 'text-davinci-003')
prompt_template = os.getenv('OPENAI_SENTIMENT_PROMPT')


class SentimentAnalyzer:
    def __init__(self, engine, prompt_template):
        self.engine = engine
        self.prompt_template = prompt_template

    def analyze_sentiment(self, comment):
        response = openai.Completion.create(
            engine=self.engine,
            prompt=self.prompt_template.format(comment=comment),
            temperature=0.5,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response.choices[0].text.strip()



engine = "text-davinci-003"
prompt_template = "Analyze the sentiment of this comment: '{comment}'"
analyzer = SentimentAnalyzer(engine, prompt_template)

comment = "This product is great!"
result = analyzer.analyze_sentiment(comment)
print(result)