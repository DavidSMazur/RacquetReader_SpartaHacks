
from openai import OpenAI
import os
from dotenv import load_dotenv
import re


load_dotenv()


os.environ['OPENAI_API_KEY'] = os.getenv('OpenAI_api_key')

client = OpenAI()
audio_out="Test, Go Blue"
count=0

split_str=re.split(r',|!|.', audio_out)

split([,.!])
while count<len(audio_out):
  prev=count
  count
  part=audio_out[prev:count]
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


