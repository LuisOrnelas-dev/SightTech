# SightTech - Sistema de Detección de Retinopatía Diabética

Sistema de inteligencia artificial para el diagnóstico temprano de retinopatía diabética con precisión superior al 95%.

## 🚀 Características

- **Análisis de Imágenes**: Procesamiento de múltiples imágenes de fondo de ojo
- **Diagnóstico Automático**: Clasificación en 5 niveles de severidad
- **Recomendaciones Personalizadas**: Basadas en síntomas y factores de riesgo
- **Reportes PDF**: Generación automática de reportes médicos
- **Interfaz Web Moderna**: Diseño responsive y fácil de usar
- **Base de Datos**: Almacenamiento seguro de pacientes y diagnósticos

## 📋 Requisitos

- Python 3.8+
- Node.js (opcional, para desarrollo)

## 🛠️ Instalación

1. **Clonar el repositorio**
```bash
git clone <repository-url>
cd SightTech
```

2. **Instalar dependencias del backend**
```bash
cd backend
pip install -r requirements.txt
```

3. **Instalar dependencias del frontend (opcional)**
```bash
npm install
```

## 🚀 Ejecución

### Backend (API)
```bash
cd backend
python app.py
```
El servidor estará disponible en `http://localhost:5002`

### Frontend (Servidor de archivos estáticos)
```bash
python app.py
```
La aplicación estará disponible en `http://localhost:5000`

## 📁 Estructura del Proyecto

```
SightTech/
├── backend/                 # API Flask
│   ├── app.py              # Servidor principal
│   ├── requirements.txt    # Dependencias Python
│   ├── uploads/           # Imágenes subidas
│   └── instance/          # Base de datos SQLite
├── assets/                # Recursos estáticos
│   ├── css/              # Estilos CSS
│   └── images/           # Imágenes del sitio
├── index.html            # Interfaz principal
├── app.py               # Servidor de archivos estáticos
└── requirements.txt     # Dependencias principales
```

## 🔧 Configuración

### Variables de Entorno
Crear archivo `.env` en el directorio backend:
```env
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///sighttech.db
```

## 📊 Uso

1. **Acceder a la aplicación**: Abrir `http://localhost:5000`
2. **Completar información del paciente**: Datos personales, síntomas y factores de riesgo
3. **Subir imágenes**: Arrastrar y soltar imágenes de fondo de ojo
4. **Analizar**: Hacer clic en "Analizar Imágenes"
5. **Revisar resultados**: Ver diagnóstico y recomendaciones
6. **Descargar reporte**: Generar PDF del análisis

## 🔬 Modelo de IA

El sistema utiliza un modelo de inteligencia artificial entrenado para detectar:
- Sin retinopatía diabética
- Retinopatía diabética leve (NPDR)
- Retinopatía diabética moderada (NPDR)
- Retinopatía diabética severa (NPDR)
- Retinopatía diabética proliferativa (PDR)

## 📈 API Endpoints

- `POST /api/analyze` - Analizar imágenes
- `GET /api/download-pdf/<id>` - Descargar reporte PDF
- `GET /api/dashboard` - Estadísticas del dashboard
- `GET /api/patients` - Lista de pacientes

## 🤝 Contribución

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.txt](LICENSE.txt) para detalles.

## ⚠️ Disclaimer

Este sistema es una herramienta de apoyo diagnóstico y no reemplaza la evaluación médica profesional. Los resultados deben ser interpretados por un médico calificado.

## 📞 Contacto

- **Email**: info@sighttech.com
- **Website**: https://sighttech.com
