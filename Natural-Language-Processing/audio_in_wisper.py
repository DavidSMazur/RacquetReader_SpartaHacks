from openai import OpenAI
import json
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OpenAI_api_key')
os.environ['OPENAI_API_KEY'] = openai_api_key

client = OpenAI()


audio_file= open("/root/hackathon/SpartaHack/spartahacks9/Michigan State University.m4a", "rb")
voice_input = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file,
  response_format="text"
)

print(voice_input)
