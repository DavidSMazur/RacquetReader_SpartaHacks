from langchain_community.llms import OpenAI
from openai import OpenAI
import names
#from NLP_Main import out
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OpenAI_api_key')
os.environ['OPENAI_API_KEY'] = openai_api_key

client = OpenAI()

out="How to hit a better serve?"

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a tennis coach, and your personality is these traits: {coaches[input_string]}. You help answer your players questions."},
    {"role": "user", "content": out}
  ]
)

audio_out=completion.choices[0].message
print(audio_out)