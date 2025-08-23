#!/bin/bash
echo "🔧 Instalando dependencias para SightTech..."

# Actualizar pip
pip install --upgrade pip

# Instalar dependencias una por una
echo "📦 Instalando Flask..."
pip install Flask==3.0.0

echo "📦 Instalando Flask-CORS..."
pip install Flask-CORS==4.0.0

echo "📦 Instalando Flask-SQLAlchemy..."
pip install Flask-SQLAlchemy==3.1.1

echo "📦 Instalando Pillow..."
pip install Pillow==10.2.0

echo "📦 Instalando numpy..."
pip install numpy==1.26.4

echo "📦 Instalando reportlab..."
pip install reportlab==4.0.9

echo "✅ Todas las dependencias instaladas correctamente" 