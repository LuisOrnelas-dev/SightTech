import json

def handler(request, context):
    """Función básica para Vercel"""
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': '{"message": "Hello World from SightTech!", "status": "success"}'
    }

# Para desarrollo local
if __name__ == "__main__":
    print("Debug function ready") 