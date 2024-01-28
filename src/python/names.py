from urllib.parse import urlparse, parse_qs
import json
from http.server import BaseHTTPRequestHandler, HTTPServer 
import cgi
coaches = {'Richard Williams': {'fatherly', 'ambitious', 'supportive', 'kind', 'humble', 
'credited his faith as a source of strength throughout each season of his life', 
'family oriented', 'american', 'williams sisters', 'resilient', 'pioneer', 'adaptable', 'trailblazer', 'progressive'},
'Toni Nadal': {'described his coaching style as hard', 'puts too much pressure because he wants his student to succeed', 
'being such a hard coach makes his pupils better tennis players', 'strict', 'stern', 'authoritarian',
'traditional', 'harsh', 'spanish', 'disciplined', 'committed', 'perfectionist', 'intense'}, 
'Patrick Mouratoglou': {'frustration into motivation', 'personal', 'custom', 'centered', 'tailored', 'passionate', 'hardworking', 'detail oriented',
'precise','charismatic', 'public speaker', 'somebody that is always trying to be better', 'exceptional tennis coach and motivator',
'greek', 'dreams come true', 'considerate', 'thoughtful', 'influential', 'one of a kind', 'revolutionary', 'positive', 'motivational', 'goal oriented'},
 'Nick Bollettieri': {'innovative', 'versatile', 'strategic', 'motivational', 'dedicated', 'experienced'},
  'Paul Annacone': {'analytical', 'calm', 'strategic', 'expertise', 'collaborative', 'patient'}}
names = []
