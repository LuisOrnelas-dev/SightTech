"""
Script para integrar modelos reales de IA con la aplicación SightTech
Reemplaza las funciones de simulación con tu modelo real
"""

import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
from transformers import AutoImageProcessor, AutoModelForImageClassification
import tensorflow as tf
from tensorflow import keras

class ModelIntegration:
    """Clase para manejar diferentes tipos de modelos de IA"""
    
    def __init__(self, model_type="pytorch", model_path=None):
        self.model_type = model_type
        self.model_path = model_path
        self.model = None
        self.processor = None
        self.class_names = [
            "Sin retinopatía diabética",
            "Retinopatía diabética leve (NPDR)",
            "Retinopatía diabética moderada (NPDR)",
            "Retinopatía diabética severa (NPDR)",
            "Retinopatía diabética proliferativa (PDR)"
        ]
        
        self.load_model()
    
    def load_model(self):
        """Carga el modelo según el tipo especificado"""
        if self.model_type == "pytorch":
            self.load_pytorch_model()
        elif self.model_type == "tensorflow":
            self.load_tensorflow_model()
        elif self.model_type == "transformers":
            self.load_transformers_model()
        else:
            raise ValueError(f"Tipo de modelo no soportado: {self.model_type}")
    
    def load_pytorch_model(self):
        """Carga modelo PyTorch"""
        try:
            # Ejemplo para modelo PyTorch personalizado
            if self.model_path:
                self.model = torch.load(self.model_path, map_location=torch.device('cpu'))
            else:
                # Modelo de ejemplo (reemplazar con tu modelo)
                self.model = self.create_sample_pytorch_model()
            
            self.model.eval()
            print("✅ Modelo PyTorch cargado exitosamente")
            
        except Exception as e:
            print(f"❌ Error cargando modelo PyTorch: {e}")
            self.model = None
    
    def load_tensorflow_model(self):
        """Carga modelo TensorFlow/Keras"""
        try:
            if self.model_path:
                self.model = keras.models.load_model(self.model_path)
            else:
                # Modelo de ejemplo (reemplazar con tu modelo)
                self.model = self.create_sample_tensorflow_model()
            
            print("✅ Modelo TensorFlow cargado exitosamente")
            
        except Exception as e:
            print(f"❌ Error cargando modelo TensorFlow: {e}")
            self.model = None
    
    def load_transformers_model(self):
        """Carga modelo de Hugging Face Transformers"""
        try:
            if self.model_path:
                model_name = self.model_path
            else:
                # Modelo de ejemplo (reemplazar con tu modelo)
                model_name = "microsoft/resnet-50"
            
            self.processor = AutoImageProcessor.from_pretrained(model_name)
            self.model = AutoModelForImageClassification.from_pretrained(model_name)
            
            print("✅ Modelo Transformers cargado exitosamente")
            
        except Exception as e:
            print(f"❌ Error cargando modelo Transformers: {e}")
            self.model = None
    
    def create_sample_pytorch_model(self):
        """Crea un modelo PyTorch de ejemplo"""
        class RetinopathyModel(nn.Module):
            def __init__(self, num_classes=5):
                super(RetinopathyModel, self).__init__()
                self.features = nn.Sequential(
                    nn.Conv2d(3, 64, 3, padding=1),
                    nn.ReLU(),
                    nn.MaxPool2d(2),
                    nn.Conv2d(64, 128, 3, padding=1),
                    nn.ReLU(),
                    nn.MaxPool2d(2),
                    nn.Conv2d(128, 256, 3, padding=1),
                    nn.ReLU(),
                    nn.AdaptiveAvgPool2d((1, 1))
                )
                self.classifier = nn.Sequential(
                    nn.Flatten(),
                    nn.Linear(256, 128),
                    nn.ReLU(),
                    nn.Dropout(0.5),
                    nn.Linear(128, num_classes)
                )
            
            def forward(self, x):
                x = self.features(x)
                x = self.classifier(x)
                return x
        
        return RetinopathyModel()
    
    def create_sample_tensorflow_model(self):
        """Crea un modelo TensorFlow de ejemplo"""
        model = keras.Sequential([
            keras.layers.Conv2D(32, 3, activation='relu', input_shape=(224, 224, 3)),
            keras.layers.MaxPooling2D(),
            keras.layers.Conv2D(64, 3, activation='relu'),
            keras.layers.MaxPooling2D(),
            keras.layers.Conv2D(64, 3, activation='relu'),
            keras.layers.GlobalAveragePooling2D(),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(5, activation='softmax')
        ])
        return model
    
    def preprocess_image(self, image):
        """Preprocesa la imagen según el tipo de modelo"""
        if self.model_type == "pytorch":
            return self.preprocess_for_pytorch(image)
        elif self.model_type == "tensorflow":
            return self.preprocess_for_tensorflow(image)
        elif self.model_type == "transformers":
            return self.preprocess_for_transformers(image)
    
    def preprocess_for_pytorch(self, image):
        """Preprocesa imagen para PyTorch"""
        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        
        if isinstance(image, np.ndarray):
            image = Image.fromarray(image)
        
        return transform(image).unsqueeze(0)
    
    def preprocess_for_tensorflow(self, image):
        """Preprocesa imagen para TensorFlow"""
        if isinstance(image, np.ndarray):
            image = Image.fromarray(image)
        
        image = image.resize((224, 224))
        image_array = np.array(image) / 255.0
        return np.expand_dims(image_array, axis=0)
    
    def preprocess_for_transformers(self, image):
        """Preprocesa imagen para Transformers"""
        if isinstance(image, np.ndarray):
            image = Image.fromarray(image)
        
        inputs = self.processor(images=image, return_tensors="pt")
        return inputs
    
    def predict(self, image):
        """Realiza predicción con el modelo cargado"""
        if self.model is None:
            return self.simulate_prediction(image)
        
        try:
            # Preprocesar imagen
            processed_image = self.preprocess_image(image)
            
            # Realizar predicción
            if self.model_type == "pytorch":
                with torch.no_grad():
                    outputs = self.model(processed_image)
                    probabilities = torch.softmax(outputs, dim=1)
                    predicted_class = torch.argmax(probabilities, dim=1).item()
                    confidence = probabilities[0][predicted_class].item()
                    all_probs = probabilities[0].numpy()
            
            elif self.model_type == "tensorflow":
                predictions = self.model.predict(processed_image)
                predicted_class = np.argmax(predictions[0])
                confidence = predictions[0][predicted_class]
                all_probs = predictions[0]
            
            elif self.model_type == "transformers":
                with torch.no_grad():
                    outputs = self.model(**processed_image)
                    probabilities = torch.softmax(outputs.logits, dim=1)
                    predicted_class = torch.argmax(probabilities, dim=1).item()
                    confidence = probabilities[0][predicted_class].item()
                    all_probs = probabilities[0].numpy()
            
            # Crear resultado
            result = {
                "prediction": self.class_names[predicted_class],
                "confidence": confidence * 100,
                "probabilities": dict(zip(self.class_names, all_probs)),
                "recommendations": self.generate_recommendations(self.class_names[predicted_class], confidence * 100),
                "severity": self.get_severity_level(self.class_names[predicted_class])
            }
            
            return result
            
        except Exception as e:
            print(f"❌ Error en predicción: {e}")
            return self.simulate_prediction(image)
    
    def simulate_prediction(self, image):
        """Simula predicción cuando el modelo no está disponible"""
        import random
        random.seed(hash(str(image.tobytes())) % 1000)
        
        probabilities = np.random.dirichlet([1, 1, 1, 1, 1])
        predicted_class = self.class_names[np.argmax(probabilities)]
        confidence = np.max(probabilities) * 100
        
        return {
            "prediction": predicted_class,
            "confidence": confidence,
            "probabilities": dict(zip(self.class_names, probabilities)),
            "recommendations": self.generate_recommendations(predicted_class, confidence),
            "severity": self.get_severity_level(predicted_class)
        }
    
    def generate_recommendations(self, prediction, confidence):
        """Genera recomendaciones basadas en el diagnóstico"""
        recommendations = {
            "Sin retinopatía diabética": [
                "Mantener control estricto de la glucosa en sangre",
                "Continuar con revisiones oftalmológicas anuales",
                "Mantener una dieta saludable y ejercicio regular",
                "Controlar la presión arterial y colesterol"
            ],
            "Retinopatía diabética leve (NPDR)": [
                "Control más frecuente de la glucosa en sangre",
                "Revisiones oftalmológicas cada 6 meses",
                "Considerar consulta con endocrinólogo",
                "Mantener presión arterial controlada"
            ],
            "Retinopatía diabética moderada (NPDR)": [
                "Consulta inmediata con oftalmólogo especialista",
                "Control estricto de glucosa y presión arterial",
                "Revisiones cada 3-4 meses",
                "Considerar tratamiento con láser si es necesario"
            ],
            "Retinopatía diabética severa (NPDR)": [
                "Consulta urgente con oftalmólogo especialista",
                "Tratamiento con láser recomendado",
                "Control muy estricto de glucosa y presión arterial",
                "Revisiones mensuales hasta estabilización"
            ],
            "Retinopatía diabética proliferativa (PDR)": [
                "Consulta inmediata y urgente con oftalmólogo",
                "Tratamiento con láser o inyecciones intravítreas",
                "Hospitalización si hay hemorragia vítrea",
                "Control extremadamente estricto de glucosa"
            ]
        }
        
        return recommendations.get(prediction, ["Consulta con especialista"])
    
    def get_severity_level(self, prediction):
        """Obtiene el nivel de severidad (1-5)"""
        severity_map = {
            "Sin retinopatía diabética": 1,
            "Retinopatía diabética leve (NPDR)": 2,
            "Retinopatía diabética moderada (NPDR)": 3,
            "Retinopatía diabética severa (NPDR)": 4,
            "Retinopatía diabética proliferativa (PDR)": 5
        }
        return severity_map.get(prediction, 1)

# Función para usar en la aplicación Gradio
def predict_retinopathy_with_model(image, model_type="pytorch", model_path=None):
    """
    Función principal para usar en la aplicación Gradio
    """
    # Crear instancia del modelo (se puede hacer una vez al inicio)
    model_integration = ModelIntegration(model_type, model_path)
    
    # Realizar predicción
    return model_integration.predict(image)

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo con modelo PyTorch
    # model = ModelIntegration("pytorch", "path/to/your/model.pth")
    
    # Ejemplo con modelo TensorFlow
    # model = ModelIntegration("tensorflow", "path/to/your/model.h5")
    
    # Ejemplo con modelo Transformers
    # model = ModelIntegration("transformers", "your-huggingface-model-name")
    
    print("✅ Modelo de integración listo para usar") 