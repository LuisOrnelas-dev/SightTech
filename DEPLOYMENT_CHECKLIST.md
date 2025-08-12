# ✅ Checklist de Despliegue - SightTech

## 🔧 Preparación del Repositorio

- [ ] ✅ Archivo `vercel.json` creado
- [ ] ✅ Carpeta `api/` con `index.py` y `chat.py`
- [ ] ✅ Archivo `config.js` para configuración centralizada
- [ ] ✅ Archivo `.gitignore` configurado
- [ ] ✅ Archivo `env.example` creado
- [ ] ✅ Script `deploy.sh` creado y ejecutable

## 🚀 Despliegue en Vercel

- [ ] ✅ Vercel CLI instalado (`npm install -g vercel`)
- [ ] ✅ Sesión iniciada en Vercel (`vercel login`)
- [ ] ✅ Archivo `.env` creado con `OPENAI_API_KEY`
- [ ] ✅ Despliegue ejecutado (`./deploy.sh` o `vercel --prod`)
- [ ] ✅ URL de producción obtenida de Vercel
- [ ] ✅ Variable `OPENAI_API_KEY` configurada en Vercel

## 🌐 Configuración de GitHub Pages

- [ ] ✅ Repositorio configurado para GitHub Pages
- [ ] ✅ Branch `main` seleccionado como fuente
- [ ] ✅ Carpeta raíz (`/`) seleccionada
- [ ] ✅ Sitio desplegado en `https://tuusername.github.io/SightTech`

## 🔗 Actualización de URLs

- [ ] ✅ URL de Vercel actualizada en `config.js`
- [ ] ✅ URLs del chatbot actualizadas en todos los archivos HTML
- [ ] ✅ URL de la app Gradio actualizada en `demoapp.html`
- [ ] ✅ Commit y push realizado a GitHub

## ✅ Pruebas en Producción

- [ ] ✅ Backend de Gradio funciona en Vercel
- [ ] ✅ Chatbot responde correctamente
- [ ] ✅ Frontend se carga en GitHub Pages
- [ ] ✅ Todas las funcionalidades funcionan
- [ ] ✅ No hay errores en la consola del navegador

## 📱 URLs Finales

- **Frontend:** `https://tuusername.github.io/SightTech`
- **Backend Gradio:** `https://tu-proyecto.vercel.app`
- **API Chatbot:** `https://tu-proyecto.vercel.app/api/chat`

## 🎯 Estado Final

- [ ] 🎉 **¡APLICACIÓN COMPLETAMENTE DESPLEGADA!**
- [ ] 🎉 **¡FUNCIONANDO EN PRODUCCIÓN!**
- [ ] 🎉 **¡ACCESIBLE DESDE CUALQUIER LUGAR!**

---

## 🚨 Problemas Comunes y Soluciones

### ❌ Error: "Module not found"
**Solución:** Verificar que `requirements.txt` tenga todas las dependencias

### ❌ Error: "OpenAI API key not found"
**Solución:** Verificar variable `OPENAI_API_KEY` en Vercel

### ❌ Error: "CORS policy"
**Solución:** Verificar que las URLs estén actualizadas correctamente

### ❌ Error: "Function not found"
**Solución:** Verificar que `vercel.json` esté configurado correctamente

---

## 📞 Soporte

Si tienes problemas durante el despliegue:
1. Revisa los logs de Vercel
2. Verifica la configuración de GitHub Pages
3. Revisa la consola del navegador
4. Consulta la documentación de Vercel y GitHub Pages

**¡Tu aplicación SightTech merece estar funcionando en producción! 🚀** 