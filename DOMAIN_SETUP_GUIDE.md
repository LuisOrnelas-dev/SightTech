# 🚀 Configuración del Dominio sighttech.mx

## ✅ Estado Actual
- ✅ Dominio `sighttech.mx` adquirido
- ✅ Acceso al dominio confirmado
- ⏳ Pendiente: Configuración DNS
- ⏳ Pendiente: Configuración en Render
- ⏳ Pendiente: Actualización de URLs en código

## 🔧 Paso 1: Configurar DNS en GoDaddy

### Opción A: Si tienes acceso directo a GoDaddy
1. Ve a [godaddy.com](https://godaddy.com) y inicia sesión
2. Ve a "Mis Productos" → "Dominios"
3. Encuentra `sighttech.mx` y haz clic en "Administrar"
4. Ve a "DNS" → "Administrar zonas"
5. Agrega estos registros CNAME:

```
Tipo: CNAME
Nombre: @
Valor: sighttechfrontend.onrender.com
TTL: 600

Tipo: CNAME  
Nombre: api
Valor: sighttech-backend.onrender.com
TTL: 600
```

### Opción B: Si alguien más maneja el DNS
Envía estas instrucciones:

```
Necesito configurar estos registros DNS para sighttech.mx:

1. CNAME Record:
   - Nombre: @ (o vacío)
   - Valor: sighttechfrontend.onrender.com
   - TTL: 600

2. CNAME Record:
   - Nombre: api
   - Valor: sighttech-backend.onrender.com  
   - TTL: 600

Esto hará que:
- sighttech.mx → Frontend (página principal)
- api.sighttech.mx → Backend (API)
```

## 🔧 Paso 2: Configurar Dominios Personalizados en Render

### Frontend (sighttechfrontend)
1. Ve a [render.com](https://render.com) → Dashboard
2. Selecciona `sighttechfrontend`
3. Ve a "Settings" → "Custom Domains"
4. Agrega: `sighttech.mx`
5. Agrega: `www.sighttech.mx`

### Backend (sighttech-backend)  
1. Ve a `sighttech-backend`
2. Ve a "Settings" → "Custom Domains"
3. Agrega: `api.sighttech.mx`

## 🔧 Paso 3: Actualizar URLs en el Código

Una vez que los dominios estén configurados, ejecutar:

```bash
python update_domain_urls.py
```

Este script actualizará automáticamente:
- `app_analysis.html`
- `dashboard.html` 
- `chatbot.js`
- `render.yaml`

## 🔧 Paso 4: Desplegar Cambios

```bash
git add .
git commit -m "Update URLs for custom domain sighttech.mx"
git push
```

## ✅ Verificación Final

1. **Frontend**: https://sighttech.mx
2. **Backend**: https://api.sighttech.mx
3. **Chatbot**: Funcionando en todas las páginas
4. **Dashboard**: Mostrando datos correctamente

## 🆘 Troubleshooting

### Si el dominio no carga:
- Verificar DNS propagation (puede tomar hasta 24 horas)
- Verificar configuración en Render
- Verificar CORS settings en backend

### Si hay errores CORS:
- Verificar que `api.sighttech.mx` esté en origins del backend
- Verificar que el frontend use `https://api.sighttech.mx`

---
**Última actualización**: Dominio adquirido, pendiente configuración DNS 