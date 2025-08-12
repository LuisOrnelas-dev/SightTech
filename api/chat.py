import json

def handler(request, context):
    """Función ultra-simple para debug"""
    
    # Configurar CORS básico
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
    }
    
    try:
        # Respuesta simple de prueba
        response_data = {
            "message": "Hello World from SightTech!",
            "status": "success",
            "debug": "Función funcionando correctamente"
        }
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps(response_data)
        }
        
    except Exception as error:
        print(f"Error: {str(error)}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({
                "error": str(error),
                "debug": "Error capturado"
            })
        }

# Para desarrollo local
if __name__ == "__main__":
    print("Debug function ready") 