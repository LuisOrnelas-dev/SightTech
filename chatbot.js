// Chatbot functionality
document.addEventListener('DOMContentLoaded', function() {
    // Wait a bit to ensure all elements are loaded
    setTimeout(function() {
        const chatbotToggle = document.getElementById('chatbot-toggle');
        const chatbotWindow = document.getElementById('chatbot-window');
        const chatbotClose = document.getElementById('chatbot-close');
        const chatbotInput = document.getElementById('chatbot-input-field');
        const chatbotSend = document.getElementById('chatbot-send');
        const chatbotMessages = document.getElementById('chatbot-messages');
        
        if (!chatbotToggle || !chatbotWindow || !chatbotClose || !chatbotInput || !chatbotSend || !chatbotMessages) {
            console.log('Chatbot elements not found');
            return;
        }
        
        // Toggle chatbot window
        chatbotToggle.addEventListener('click', () => {
            chatbotWindow.style.display = chatbotWindow.style.display === 'none' ? 'flex' : 'none';
        });
        
        chatbotClose.addEventListener('click', () => {
            chatbotWindow.style.display = 'none';
        });
        
        // Send message
        function sendMessage() {
            const message = chatbotInput.value.trim();
            if (!message) return;
            
            // Add user message
            addMessage(message, 'user');
            chatbotInput.value = '';
            
            // Send to backend
            fetch('https://sighttech-backend.onrender.com/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: message,
                    context: {}
                })
            })
            .then(response => response.json())
            .then(data => {
                addMessage(data.response, 'bot');
            })
            .catch(error => {
                console.error('Error:', error);
                addMessage('Lo siento, tuve un problema procesando tu mensaje. ¿Podrías intentar de nuevo?', 'bot');
            });
        }
        
        // Add message to chat
        function addMessage(text, sender) {
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${sender}-message`;
            
            const avatar = sender === 'bot' ? 'fas fa-robot' : 'fas fa-user';
            
            messageDiv.innerHTML = `
                <div class="message-content">
                    <i class="${avatar} message-avatar"></i>
                    <div class="message-text">${text}</div>
                </div>
            `;
            
            chatbotMessages.appendChild(messageDiv);
            chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
        }
        
        // Event listeners for chatbot
        chatbotSend.addEventListener('click', sendMessage);
        chatbotInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
        
        console.log('Chatbot initialized successfully');
    }, 1000);
}); 