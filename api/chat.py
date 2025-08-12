from http.server import BaseHTTPRequestHandler
import json
import os
from openai import OpenAI

def handler(request, context):
    """Función principal para Vercel"""
    
    # Configurar CORS
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
    
    # Manejar preflight CORS
    if request.method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': ''
        }
    
    # Solo procesar peticiones POST
    if request.method != 'POST':
        return {
            'statusCode': 405,
            'headers': headers,
            'body': json.dumps({'error': 'Method not allowed'})
        }
    
    try:
        # Obtener el cuerpo de la petición
        body = request.body
        if isinstance(body, str):
            request_data = json.loads(body)
        else:
            request_data = json.loads(body.decode('utf-8'))
        
        # Obtener el prompt del usuario
        prompt = request_data.get('prompt', '')
        
        if not prompt:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'Prompt is required'})
            }
        
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
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps(response_data)
        }
        
    except Exception as error:
        print(f"Error: {str(error)}")
        error_response = {
            "error": str(error),
            "bot": "Lo siento, hubo un error procesando tu mensaje. Por favor, intenta de nuevo."
        }
        
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps(error_response)
        }

# Para desarrollo local
if __name__ == "__main__":
    from http.server import HTTPServer, BaseHTTPRequestHandler
    import json
    
    class LocalHandler(BaseHTTPRequestHandler):
        def do_POST(self):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            request_data = json.loads(post_data.decode('utf-8'))
            
            # Simular la función de Vercel
            mock_request = type('MockRequest', (), {
                'method': 'POST',
                'body': json.dumps(request_data)
            })()
            
            result = handler(mock_request, None)
            self.wfile.write(result['body'].encode())
    
    server = HTTPServer(('localhost', 4000), LocalHandler)
    print("Chat server started on http://localhost:4000")
    server.serve_forever() 