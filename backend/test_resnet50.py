"""
Script para probar el modelo ResNet50
"""

import numpy as np
from PIL import Image
import os

def create_test_image():
    """Crear una imagen de prueba"""
    # Crear una imagen sintética de 224x224 píxeles
    img_array = np.random.randint(0, 255, (224, 224, 3), dtype=np.uint8)
    img = Image.fromarray(img_array)
    return img

def test_resnet50_model():
    """Probar el modelo ResNet50"""
    print("🧪 Probando modelo ResNet50...")
    
    try:
        # Importar el modelo
        from real_ai_model import RetinopathyResNet50Model
        
        # Crear instancia del modelo
        print("🔄 Inicializando modelo ResNet50...")
        model = RetinopathyResNet50Model()
        
        # Crear imágenes de prueba
        print("🔄 Creando imágenes de prueba...")
        test_images = [create_test_image() for _ in range(3)]
        
        # Realizar predicción
        print("🔄 Realizando predicción...")
        result = model.predict_multiple_images(test_images)
        
        if result:
            print("✅ Predicción exitosa!")
            print(f"📊 Diagnóstico: {result['prediction']}")
            print(f"🎯 Confianza: {result['confidence']:.1f}%")
            print(f"⚠️ Severidad: {result['severity']}/5")
            print(f"📸 Imágenes analizadas: {result['images_analyzed']}")
            
            print("\n📋 Resultados individuales:")
            for i, individual in enumerate(result['individual_results']):
                print(f"  Imagen {i+1}: {individual['prediction']} ({individual['confidence']:.1f}%)")
            
            return True
        else:
            print("❌ Error en la predicción")
            return False
            
    except Exception as e:
        print(f"❌ Error probando modelo: {e}")
        return False

def test_model_integration():
    """Probar la integración con el sistema principal"""
    print("\n🔗 Probando integración con sistema principal...")
    
    try:
        from ai_model import predict_retinopathy_with_ai
        
        # Crear imágenes de prueba
        test_images = [create_test_image() for _ in range(2)]
        
        # Realizar predicción
        result = predict_retinopathy_with_ai(test_images)
        
        if result:
            print("✅ Integración exitosa!")
            print(f"📊 Resultado: {result['prediction']}")
            print(f"🎯 Confianza: {result['confidence']:.1f}%")
            return True
        else:
            print("❌ Error en integración")
            return False
            
    except Exception as e:
        print(f"❌ Error en integración: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Iniciando pruebas del modelo ResNet50...")
    
    # Probar modelo directamente
    success1 = test_resnet50_model()
    
    # Probar integración
    success2 = test_model_integration()
    
    if success1 and success2:
        print("\n🎉 ¡Todas las pruebas exitosas!")
        print("✅ El modelo ResNet50 está listo para usar")
    else:
        print("\n⚠️ Algunas pruebas fallaron")
        print("🔧 Revisar configuración del modelo") 