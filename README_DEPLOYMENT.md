# 🚀 Guía de Despliegue - SightTech

## 📋 Resumen del Despliegue Híbrido

- **Backend (IA + Chatbot):** Vercel (Gratis)
- **Frontend:** GitHub Pages (Gratis)
- **Dominio:** `tuusername.github.io/SightTech`

---

## 🔧 PASO 1: Preparar el Repositorio

### 1.1 Verificar archivos de configuración
Asegúrate de tener estos archivos en tu repositorio:
- ✅ `vercel.json` - Configuración de Vercel
- ✅ `api/index.py` - API principal de Gradio
- ✅ `api/chat.py` - API del chatbot
- ✅ `requirements.txt` - Dependencias de Python
- ✅ `env.example` - Variables de entorno de ejemplo

### 1.2 Variables de entorno
Crea un archivo `.env` en tu repositorio local (NO lo subas a GitHub):
```bash
OPENAI_API_KEY=tu_api_key_real_de_openai
```

---

## 🚀 PASO 2: Desplegar Backend en Vercel

### 2.1 Instalar Vercel CLI
```bash
npm install -g vercel
```

### 2.2 Iniciar sesión en Vercel
```bash
vercel login
```

### 2.3 Desplegar el proyecto
```bash
vercel
```

**Durante el despliegue, Vercel te preguntará:**
- Project name: `sighttech-backend`
- Directory: `.` (directorio actual)
- Override settings: `N` (no)

### 2.4 Configurar variables de entorno
En el dashboard de Vercel:
1. Ve a tu proyecto
2. Settings → Environment Variables
3. Agrega: `OPENAI_API_KEY` = `tu_api_key_real`

### 2.5 Obtener la URL de producción
Vercel te dará una URL como: `https://sighttech-backend.vercel.app`

---

## 🌐 PASO 3: Configurar GitHub Pages

### 3.1 Verificar configuración del repositorio
1. Ve a tu repositorio en GitHub
2. Settings → Pages
3. Source: `Deploy from a branch`
4. Branch: `main` (o `master`)
5. Folder: `/ (root)`

### 3.2 Actualizar URLs en el frontend
Una vez que tengas la URL de Vercel, actualiza estos archivos:
- `app.js`
- `beautiful.html`
- `demoapp.html`
- `index.html`

**Cambiar todas las URLs de `localhost:4000` por tu URL de Vercel + `/api/chat`**

---

## 🔗 PASO 4: Conectar Frontend y Backend

### 4.1 Actualizar URLs del chatbot
En todos los archivos HTML, cambiar:
```javascript
// ANTES
const response = await fetch('http://localhost:4000', {

// DESPUÉS
const response = await fetch('https://tu-proyecto.vercel.app/api/chat', {
```

### 4.2 Actualizar URL de la app Gradio
En `demoapp.html`, cambiar:
```html
<!-- ANTES -->
<iframe src="http://localhost:7860">

<!-- DESPUÉS -->
<iframe src="https://tu-proyecto.vercel.app">
```

---

## ✅ PASO 5: Probar en Producción

### 5.1 Verificar el backend
- Visita: `https://tu-proyecto.vercel.app`
- Deberías ver la interfaz de Gradio

### 5.2 Verificar el chatbot
- Visita: `https://tu-proyecto.vercel.app/api/chat`
- Debería responder a peticiones POST

### 5.3 Verificar el frontend
- Visita: `https://tuusername.github.io/SightTech`
- Todo debería funcionar correctamente

---

## 🐛 Solución de Problemas Comunes

### Error: "Module not found"
- Verifica que `requirements.txt` tenga todas las dependencias
- Asegúrate de que `vercel.json` esté configurado correctamente

### Error: "OpenAI API key not found"
- Verifica que la variable `OPENAI_API_KEY` esté configurada en Vercel
- Asegúrate de que el archivo `.env` no esté en GitHub

### Error: "CORS policy"
- El backend ya está configurado para permitir CORS
- Verifica que las URLs estén actualizadas correctamente

---

## 📱 URLs Finales

- **Frontend:** `https://tuusername.github.io/SightTech`
- **Backend Gradio:** `https://tu-proyecto.vercel.app`
- **API Chatbot:** `https://tu-proyecto.vercel.app/api/chat`

---

## 🎉 ¡Listo!

Tu aplicación SightTech estará funcionando completamente en producción con:
- ✅ Backend de IA desplegado en Vercel
- ✅ Chatbot funcionando con OpenAI
- ✅ Frontend desplegado en GitHub Pages
- ✅ Todo funcionando de forma gratuita

**¿Necesitas ayuda con algún paso específico?** 