from http.server import BaseHTTPRequestHandler
import json
import os
from openai import OpenAI

class ChatHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Configurar CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        try:
            # Leer el cuerpo de la petición
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            request_data = json.loads(post_data.decode('utf-8'))
            
            # Obtener el prompt del usuario
            prompt = request_data.get('prompt', '')
            
            # Configurar OpenAI
            openai = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
            
            # Crear la respuesta
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0,
                max_tokens=3000,
            )
            
            # Preparar la respuesta
            bot_response = response.choices[0].message.content
            
            response_data = {
                "bot": bot_response
            }
            
            self.wfile.write(json.dumps(response_data).encode())
            
        except Exception as error:
            error_response = {
                "error": str(error),
                "bot": "Lo siento, hubo un error procesando tu mensaje. Por favor, intenta de nuevo."
            }
            self.wfile.write(json.dumps(error_response).encode())
    
    def do_OPTIONS(self):
        # Manejar preflight CORS
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

# Para Vercel
def handler(request, context):
    return ChatHandler().do_POST()

# Para desarrollo local
if __name__ == "__main__":
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 4000), ChatHandler)
    print("Chat server started on http://localhost:4000")
    server.serve_forever() 