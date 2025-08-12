from app import create_interface
import gradio as gr

# Crear la interfaz de Gradio
demo = create_interface()

# Para Vercel, necesitamos exportar la app
app = demo.app

# También exportar la interfaz completa para uso directo
if __name__ == "__main__":
    demo.launch() 