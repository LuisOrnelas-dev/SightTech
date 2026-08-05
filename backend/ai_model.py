"""
Punto de entrada para predicción con IA — delega a real_ai_model.py
"""

from real_ai_model import predict_retinopathy_with_real_ai


def predict_retinopathy_with_ai(images):
    return predict_retinopathy_with_real_ai(images)
