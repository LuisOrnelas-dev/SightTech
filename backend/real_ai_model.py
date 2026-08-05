"""
ResNet50 entrenado en APTOS 2019 — HuggingFace: sakshamkr1/ResNet50-APTOS-DR
Licencia: CC-BY-NC 4.0 (uso académico/no comercial)
"""

import os
import numpy as np
from PIL import Image
import torch
import torchvision.transforms as transforms
from huggingface_hub import hf_hub_download

MODEL_REPO  = "sakshamkr1/ResNet50-APTOS-DR"
MODEL_FILE  = "diabetic_retinopathy_full_model.pth"
MODEL_CACHE = os.path.join(os.path.dirname(__file__), MODEL_FILE)

CLASS_NAMES = [
    "Sin retinopatía diabética",
    "Retinopatía diabética leve (NPDR)",
    "Retinopatía diabética moderada (NPDR)",
    "Retinopatía diabética severa (NPDR)",
    "Retinopatía diabética proliferativa (PDR)"
]

TRANSFORM = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

_model = None


def _load_model():
    global _model
    if _model is not None:
        return _model

    if not os.path.exists(MODEL_CACHE):
        print(f"⬇️  Descargando modelo desde HuggingFace ({MODEL_REPO})...")
        hf_hub_download(
            repo_id=MODEL_REPO,
            filename=MODEL_FILE,
            local_dir=os.path.dirname(__file__)
        )
        print("✅ Modelo descargado correctamente")

    print("🔄 Cargando ResNet50-APTOS en memoria...")
    _model = torch.load(MODEL_CACHE, map_location=torch.device('cpu'), weights_only=False)
    _model.eval()
    print("✅ Modelo listo para predicción")
    return _model


def predict_retinopathy_with_real_ai(images):
    """Predicción con ResNet50 entrenado en APTOS 2019 (5 clases ICDRD)"""
    model = _load_model()

    individual_results = []
    for i, img in enumerate(images):
        if img.mode != 'RGB':
            img = img.convert('RGB')

        tensor = TRANSFORM(img).unsqueeze(0)

        with torch.no_grad():
            outputs = model(tensor)
            probs = torch.softmax(outputs, dim=1)[0].cpu().numpy()

        class_idx = int(np.argmax(probs))
        confidence = float(probs[class_idx] * 100)

        individual_results.append({
            "image_index": i,
            "prediction": CLASS_NAMES[class_idx],
            "confidence": confidence,
            "probabilities": dict(zip(CLASS_NAMES, probs.tolist())),
            "severity": class_idx + 1
        })

    max_severity = max(r['severity'] for r in individual_results)
    final = next(r for r in individual_results if r['severity'] == max_severity)
    avg_confidence = sum(r['confidence'] for r in individual_results) / len(individual_results)

    return {
        "prediction": final['prediction'],
        "confidence": avg_confidence,
        "probabilities": final['probabilities'],
        "severity": max_severity,
        "individual_results": individual_results,
        "images_analyzed": len(images)
    }
