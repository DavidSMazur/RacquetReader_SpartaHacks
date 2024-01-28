from langchain_community.llms import OpenAI
from openai import OpenAI
from names import coaches
#from NLP_Main import out
import os
from dotenv import load_dotenv
import jsonify
from app import input_string

load_dotenv()

openai_api_key = os.getenv('OpenAI_api_key')
os.environ['OPENAI_API_KEY'] = openai_api_key
def prompt():


    # Get the string from the request data
  
  client = OpenAI()

  out=input_string 

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a tennis coach, and your personality is these traits: {coaches[input_string]}. You help answer your players questions."},
      {"role": "user", "content": out}
    ]
  )

  audio_out=completion.choices[0].message



    # Process the string (you can replace this with your processing logic)
  AI_response = completion.choices[0].message
  print(AI_response)
    # Return the processed string as a JSON response
  return jsonify({'AI response': AI_response}), 200

prompt()
