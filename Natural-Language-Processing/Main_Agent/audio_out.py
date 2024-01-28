
from openai import OpenAI
import os
from dotenv import load_dotenv
from coachify import audio_out

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OpenAI_api_key')

client = OpenAI()

split_str=audio_out.split(".")

for sec in split_str:
  
  
  response += client.audio.speech.create(
      model="tts-1",
      voice="alloy",
      input=part,
)


#--------------------------
#pyaudio

from openai import OpenAI

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Hello world! This is a streaming test.",
)

response.stream_to_file("output.mp3")


