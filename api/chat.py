from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        
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
        
        return jsonify({
            "bot": bot_response
        })
        
    except Exception as error:
        print(f"Error: {str(error)}")
        return jsonify({
            "error": str(error),
            "bot": "Lo siento, hubo un error procesando tu mensaje. Por favor, intenta de nuevo."
        }), 500

@app.route('/')
def health():
    return jsonify({"status": "Chatbot API running"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000))) 