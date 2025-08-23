# 🚀 Deploy SightTech en Render

## 📋 Pasos para Deploy

### 1. **Preparación del Repositorio**
- ✅ Archivos de configuración creados
- ✅ URLs actualizadas para producción
- ✅ Scripts de inicio configurados

### 2. **Deploy en Render**

#### **Backend (Python/Flask)**
1. Ve a [render.com](https://render.com)
2. Crea una nueva cuenta o inicia sesión
3. Haz clic en "New +" → "Web Service"
4. Conecta tu repositorio de GitHub
5. Configura:
   - **Name**: `sighttech-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `cd backend && python app.py`
   - **Plan**: Free

#### **Frontend (Static Site)**
1. En Render, haz clic en "New +" → "Static Site"
2. Conecta el mismo repositorio
3. Configura:
   - **Name**: `sighttech-frontend`
   - **Build Command**: `echo "Build complete"`
   - **Publish Directory**: `.`
   - **Plan**: Free

### 3. **Variables de Entorno**
En el backend, agrega:
- `FLASK_ENV=production`
- `PORT=10000`

### 4. **URLs Finales**
- **Frontend**: `https://sighttech-frontend.onrender.com`
- **Backend**: `https://sighttech-backend.onrender.com`

## 🎯 Para Demo UNITEC

### **Credenciales de Acceso:**
- **Usuario**: `doctor`
- **Contraseña**: `sighttech2024`

### **Funcionalidades Destacadas:**
- ✅ IA médica para retinopatía diabética
- ✅ Chatbot con asistencia médica
- ✅ Generación automática de PDFs
- ✅ Dashboard con estadísticas
- ✅ Interfaz médica profesional

## 🔧 Troubleshooting

### **Si el backend no inicia:**
1. Verifica que `requirements.txt` esté en `/backend/`
2. Asegúrate de que `app.py` esté en `/backend/`
3. Revisa los logs en Render

### **Si el frontend no carga:**
1. Verifica que las URLs apunten al backend correcto
2. Revisa la consola del navegador
3. Asegúrate de que CORS esté configurado

## 📞 Soporte
Para problemas técnicos, revisa los logs en Render Dashboard. 