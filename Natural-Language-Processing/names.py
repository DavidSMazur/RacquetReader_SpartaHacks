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

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the query parameters from the request URL
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        # Extract the 'name' parameter from the query parameters
        name = query_params.get('name', [''])[0]

        # Store the name in the names list
        names.append(name)

        # Send a response back to the client
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = {'message': f'Name "{name}" stored successfully'}
        self.wfile.write(json.dumps(response).encode('utf-8'))

def run_server(server_class=HTTPServer, handler_class=HTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

