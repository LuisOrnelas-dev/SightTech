// 🚀 Configuración de SightTech para Producción
// Actualiza estas URLs después de desplegar en Vercel

const CONFIG = {
    // URLs del Backend (Vercel)
    BACKEND_URL: 'https://sighttech-backend.vercel.app', // ← URL ACTUALIZADA
    CHAT_API_URL: 'https://sighttech-backend.vercel.app/api/chat', // ← URL ACTUALIZADA
    
    // URLs del Frontend (GitHub Pages)
    FRONTEND_URL: 'https://tuusername.github.io/SightTech', // ← CAMBIA ESTA URL
    
    // Configuración de la aplicación
    APP_NAME: 'SightTech',
    APP_VERSION: '1.0.0',
    
    // Configuración del chatbot
    CHATBOT_NAME: 'SightTech Assistant',
    CHATBOT_WELCOME: '¡Hola! Soy el asistente virtual de SightTech. ¿En qué puedo ayudarte?',
    
    // Configuración de la IA
    AI_MODEL: 'gpt-3.5-turbo',
    MAX_TOKENS: 3000,
    
    // Configuración de la interfaz
    THEME: {
        primary: '#2563eb',
        secondary: '#7c3aed',
        accent: '#10b981'
    }
};

// Función para obtener la URL completa del backend
function getBackendUrl(path = '') {
    return CONFIG.BACKEND_URL + path;
}

// Función para obtener la URL completa de la API de chat
function getChatApiUrl() {
    return CONFIG.CHAT_API_URL;
}

// Función para obtener la URL del frontend
function getFrontendUrl(path = '') {
    return CONFIG.FRONTEND_URL + path;
}

// Exportar configuración para uso en otros archivos
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONFIG;
} else {
    // Para uso en el navegador
    window.SightTechConfig = CONFIG;
    window.getBackendUrl = getBackendUrl;
    window.getChatApiUrl = getChatApiUrl;
    window.getFrontendUrl = getFrontendUrl;
} 