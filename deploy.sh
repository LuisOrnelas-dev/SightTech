#!/bin/bash

echo "🚀 Iniciando despliegue de SightTech..."

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Verificar si Vercel CLI está instalado
if ! command -v vercel &> /dev/null; then
    echo -e "${RED}❌ Vercel CLI no está instalado${NC}"
    echo -e "${YELLOW}Instalando Vercel CLI...${NC}"
    npm install -g vercel
else
    echo -e "${GREEN}✅ Vercel CLI ya está instalado${NC}"
fi

# Verificar si hay un archivo .env
if [ ! -f .env ]; then
    echo -e "${YELLOW}⚠️  Archivo .env no encontrado${NC}"
    echo -e "${YELLOW}Por favor, crea un archivo .env con tu OPENAI_API_KEY${NC}"
    echo "OPENAI_API_KEY=tu_api_key_aqui" > .env
    echo -e "${RED}❌ Edita el archivo .env con tu API key real antes de continuar${NC}"
    exit 1
fi

# Verificar si el usuario está logueado en Vercel
echo -e "${YELLOW}🔐 Verificando sesión de Vercel...${NC}"
if ! vercel whoami &> /dev/null; then
    echo -e "${YELLOW}Iniciando sesión en Vercel...${NC}"
    vercel login
else
    echo -e "${GREEN}✅ Ya estás logueado en Vercel${NC}"
fi

# Desplegar en Vercel
echo -e "${YELLOW}🚀 Desplegando en Vercel...${NC}"
vercel --prod

echo -e "${GREEN}✅ ¡Despliegue completado!${NC}"
echo -e "${YELLOW}📋 Próximos pasos:${NC}"
echo "1. Copia la URL de producción que te dio Vercel"
echo "2. Actualiza las URLs en los archivos HTML del frontend"
echo "3. Haz commit y push a GitHub"
echo "4. Configura GitHub Pages en tu repositorio"
echo ""
echo -e "${GREEN}🎉 ¡Tu aplicación estará funcionando en producción!${NC}" 