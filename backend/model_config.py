"""
Configuración del modelo de IA para retinopatía diabética
"""

# Configuración del modelo
MODEL_CONFIG = {
    'model_type': 'resnet50',  # Tipo de modelo a usar
    'input_size': (224, 224),  # Tamaño de entrada de las imágenes
    'batch_size': 1,           # Tamaño del batch para predicción
    'use_gpu': True,           # Usar GPU si está disponible
    'confidence_threshold': 0.7,  # Umbral de confianza mínimo
}

# Clases de retinopatía
RETINOPATHY_CLASSES = [
    "Sin retinopatía diabética",
    "Retinopatía diabética leve (NPDR)",
    "Retinopatía diabética moderada (NPDR)",
    "Retinopatía diabética severa (NPDR)",
    "Retinopatía diabética proliferativa (PDR)"
]

# Mapeo de severidad
SEVERITY_MAPPING = {
    "Sin retinopatía diabética": 1,
    "Retinopatía diabética leve (NPDR)": 2,
    "Retinopatía diabética moderada (NPDR)": 3,
    "Retinopatía diabética severa (NPDR)": 4,
    "Retinopatía diabética proliferativa (PDR)": 5
}

# Configuración de preprocesamiento
PREPROCESSING_CONFIG = {
    'normalize': True,
    'augment': False,
    'resize_method': 'bilinear',
    'color_mode': 'rgb'
}

# Rutas de modelos (para futuras implementaciones)
MODEL_PATHS = {
    'resnet50': 'models/resnet50_retinopathy.h5',
    'densenet121': 'models/densenet121_retinopathy.h5',
    'efficientnet': 'models/efficientnet_retinopathy.h5',
    'custom': 'models/custom_retinopathy.h5'
}

# Configuración de logging
LOGGING_CONFIG = {
    'log_predictions': True,
    'log_confidence': True,
    'save_predictions': False,
    'log_level': 'INFO'
} 