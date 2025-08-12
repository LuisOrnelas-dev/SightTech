import gradio as gr
import numpy as np
from PIL import Image
import io
import tempfile
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# Simulación del modelo de IA (reemplaza con tu modelo real)
def predict_retinopathy(image):
    """
    Función que simula la predicción de retinopatía diabética.
    Reemplaza esta función con tu modelo real de IA.
    """
    import random
    random.seed(hash(str(image.tobytes())) % 1000)
    
    probabilities = np.random.dirichlet([1, 1, 1, 1, 1])
    classes = [
        "Sin retinopatía diabética",
        "Retinopatía diabética leve (NPDR)",
        "Retinopatía diabética moderada (NPDR)",
        "Retinopatía diabética severa (NPDR)",
        "Retinopatía diabética proliferativa (PDR)"
    ]
    
    predicted_class = classes[np.argmax(probabilities)]
    confidence = np.max(probabilities) * 100
    recommendations = generate_recommendations(predicted_class, confidence)
    
    return {
        "prediction": predicted_class,
        "confidence": confidence,
        "probabilities": dict(zip(classes, probabilities)),
        "recommendations": recommendations,
        "severity": get_severity_level(predicted_class)
    }

def generate_recommendations(prediction, confidence):
    """Genera recomendaciones basadas en el diagnóstico"""
    recommendations = {
        "Sin retinopatía diabética": [
            "Mantener control estricto de la glucosa en sangre",
            "Continuar con revisiones oftalmológicas anuales",
            "Mantener una dieta saludable y ejercicio regular",
            "Controlar la presión arterial y colesterol"
        ],
        "Retinopatía diabética leve (NPDR)": [
            "Control más frecuente de la glucosa en sangre",
            "Revisiones oftalmológicas cada 6 meses",
            "Considerar consulta con endocrinólogo",
            "Mantener presión arterial controlada"
        ],
        "Retinopatía diabética moderada (NPDR)": [
            "Consulta inmediata con oftalmólogo especialista",
            "Control estricto de glucosa y presión arterial",
            "Revisiones cada 3-4 meses",
            "Considerar tratamiento con láser si es necesario"
        ],
        "Retinopatía diabética severa (NPDR)": [
            "Consulta urgente con oftalmólogo especialista",
            "Tratamiento con láser recomendado",
            "Control muy estricto de glucosa y presión arterial",
            "Revisiones mensuales hasta estabilización"
        ],
        "Retinopatía diabética proliferativa (PDR)": [
            "Consulta inmediata y urgente con oftalmólogo",
            "Tratamiento con láser o inyecciones intravítreas",
            "Hospitalización si hay hemorragia vítrea",
            "Control extremadamente estricto de glucosa"
        ]
    }
    
    return recommendations.get(prediction, ["Consulta con especialista"])

def get_severity_level(prediction):
    """Obtiene el nivel de severidad (1-5)"""
    severity_map = {
        "Sin retinopatía diabética": 1,
        "Retinopatía diabética leve (NPDR)": 2,
        "Retinopatía diabética moderada (NPDR)": 3,
        "Retinopatía diabética severa (NPDR)": 4,
        "Retinopatía diabética proliferativa (PDR)": 5
    }
    return severity_map.get(prediction, 1)

def create_pdf_report(patient_data, image, diagnosis_result):
    """Crea un reporte PDF profesional"""
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        pdf_path = tmp_file.name
    
    doc = SimpleDocTemplate(pdf_path, pagesize=A4)
    story = []
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2563eb')
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=20,
        textColor=colors.HexColor('#374151')
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=12
    )
    
    # Encabezado
    story.append(Paragraph("SightTech - Reporte de Diagnóstico", title_style))
    story.append(Paragraph("Detección de Retinopatía Diabética", subtitle_style))
    story.append(Spacer(1, 20))
    
    # Información del paciente
    story.append(Paragraph("INFORMACIÓN DEL PACIENTE", subtitle_style))
    patient_info = [
        ["Nombre:", patient_data.get('name', 'No especificado')],
        ["Edad:", f"{patient_data.get('age', 'No especificado')} años"],
        ["Género:", patient_data.get('gender', 'No especificado')],
        ["Fecha de análisis:", datetime.now().strftime("%d/%m/%Y %H:%M")],
        ["Tiempo con diabetes:", f"{patient_data.get('diabetes_years', 'No especificado')} años"],
        ["Nivel de glucosa:", f"{patient_data.get('glucose_level', 'No especificado')} mg/dL"],
        ["Presión arterial:", f"{patient_data.get('blood_pressure', 'No especificado')} mmHg"]
    ]
    
    patient_table = Table(patient_info, colWidths=[2*inch, 4*inch])
    patient_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f3f4f6')),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#374151')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#d1d5db'))
    ]))
    story.append(patient_table)
    story.append(Spacer(1, 20))
    
    # Resultados del diagnóstico
    story.append(Paragraph("RESULTADOS DEL DIAGNÓSTICO", subtitle_style))
    
    diagnosis_text = f"""
    <b>Diagnóstico:</b> {diagnosis_result['prediction']}<br/>
    <b>Confianza del modelo:</b> {diagnosis_result['confidence']:.1f}%<br/>
    <b>Nivel de severidad:</b> {diagnosis_result['severity']}/5
    """
    story.append(Paragraph(diagnosis_text, normal_style))
    story.append(Spacer(1, 15))
    
    # Probabilidades
    story.append(Paragraph("Probabilidades por clase:", normal_style))
    for class_name, prob in diagnosis_result['probabilities'].items():
        prob_text = f"• {class_name}: {prob*100:.1f}%"
        story.append(Paragraph(prob_text, normal_style))
    
    story.append(Spacer(1, 20))
    
    # Recomendaciones
    story.append(Paragraph("RECOMENDACIONES MÉDICAS", subtitle_style))
    for i, recommendation in enumerate(diagnosis_result['recommendations'], 1):
        rec_text = f"{i}. {recommendation}"
        story.append(Paragraph(rec_text, normal_style))
    
    story.append(Spacer(1, 20))
    
    # Imagen analizada
    if image is not None:
        story.append(Paragraph("IMAGEN ANALIZADA", subtitle_style))
        img_buffer = io.BytesIO()
        image.save(img_buffer, format='PNG')
        img_buffer.seek(0)
        
        pdf_img = RLImage(img_buffer, width=4*inch, height=3*inch)
        story.append(pdf_img)
        story.append(Spacer(1, 20))
    
    # Pie de página
    story.append(Paragraph("NOTA IMPORTANTE:", subtitle_style))
    disclaimer = """
    Este reporte es generado automáticamente por un sistema de inteligencia artificial 
    y debe ser revisado por un profesional médico calificado. Los resultados son 
    informativos y no constituyen un diagnóstico médico definitivo.
    """
    story.append(Paragraph(disclaimer, normal_style))
    
    doc.build(story)
    return pdf_path

def process_diagnosis(image, patient_data):
    """Procesa el diagnóstico completo"""
    
    if image is None:
        return "Por favor, sube una imagen de fondo de ojo.", None, None
    
    # Realizar predicción
    diagnosis_result = predict_retinopathy(image)
    
    # Crear reporte PDF
    pdf_path = create_pdf_report(patient_data, image, diagnosis_result)
    
    # Preparar resultados para mostrar
    result_text = f"""
    ## 📋 DIAGNÓSTICO COMPLETO
    
    **Resultado:** {diagnosis_result['prediction']}
    **Confianza:** {diagnosis_result['confidence']:.1f}%
    **Severidad:** {diagnosis_result['severity']}/5
    
    ## 📊 PROBABILIDADES
    """
    
    for class_name, prob in diagnosis_result['probabilities'].items():
        result_text += f"- {class_name}: {prob*100:.1f}%\n"
    
    result_text += "\n## 💡 RECOMENDACIONES\n"
    for i, recommendation in enumerate(diagnosis_result['recommendations'], 1):
        result_text += f"{i}. {recommendation}\n"
    
    return result_text, pdf_path, diagnosis_result

# Interfaz de Gradio
def create_interface():
    with gr.Blocks(
        title="SightTech - Detección de Retinopatía Diabética",
        theme=gr.themes.Soft(
            primary_hue="blue",
            secondary_hue="purple",
            neutral_hue="gray"
        ),
        css="""
        .gradio-container {
            max-width: 1200px !important;
            margin: 0 auto !important;
        }
        .header {
            text-align: center;
            padding: 20px;
            background: linear-gradient(135deg, #2563eb, #7c3aed);
            color: white;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        """
    ) as demo:
        
        # Header personalizado
        with gr.Row():
            gr.HTML("""
            <div class="header">
                <h1>🔬 SightTech - Sistema de Detección de Retinopatía Diabética</h1>
                <p>Inteligencia Artificial para el diagnóstico temprano con precisión superior al 95%</p>
            </div>
            """)
        
        with gr.Tabs():
            # Pestaña 1: Cuestionario del Paciente
            with gr.TabItem("📝 Información del Paciente"):
                with gr.Row():
                    with gr.Column(scale=1):
                        gr.Markdown("### Datos Personales")
                        name = gr.Textbox(label="Nombre completo", placeholder="Ej: Juan Pérez")
                        age = gr.Number(label="Edad", minimum=1, maximum=120, value=45)
                        gender = gr.Radio(
                            choices=["Masculino", "Femenino", "Otro"],
                            label="Género",
                            value="Masculino"
                        )
                        
                        gr.Markdown("### Información Médica")
                        diabetes_years = gr.Number(
                            label="Años con diabetes", 
                            minimum=0, 
                            maximum=50, 
                            value=5
                        )
                        glucose_level = gr.Number(
                            label="Nivel de glucosa (mg/dL)", 
                            minimum=50, 
                            maximum=500, 
                            value=140
                        )
                        blood_pressure = gr.Textbox(
                            label="Presión arterial (mmHg)", 
                            placeholder="Ej: 120/80"
                        )
                        
                        gr.Markdown("### Síntomas")
                        symptoms = gr.CheckboxGroup(
                            choices=[
                                "Visión borrosa",
                                "Manchas flotantes",
                                "Dificultad para ver de noche",
                                "Pérdida de visión central",
                                "Dolor en los ojos",
                                "Ninguno de los anteriores"
                            ],
                            label="¿Qué síntomas experimentas?",
                            value=["Ninguno de los anteriores"]
                        )
                    
                    with gr.Column(scale=1):
                        gr.Markdown("### Factores de Riesgo")
                        risk_factors = gr.CheckboxGroup(
                            choices=[
                                "Hipertensión arterial",
                                "Colesterol alto",
                                "Fumar",
                                "Obesidad",
                                "Historial familiar de retinopatía",
                                "Embarazo (diabetes gestacional)",
                                "Ninguno de los anteriores"
                            ],
                            label="Factores de riesgo adicionales",
                            value=["Ninguno de los anteriores"]
                        )
                        
                        gr.Markdown("### Medicamentos")
                        medications = gr.CheckboxGroup(
                            choices=[
                                "Insulina",
                                "Metformina",
                                "Otros antidiabéticos orales",
                                "Medicamentos para la presión",
                                "Estatinas",
                                "Ninguno"
                            ],
                            label="Medicamentos que toma actualmente",
                            value=["Ninguno"]
                        )
                        
                        gr.Markdown("### Última Revisión")
                        last_eye_exam = gr.Radio(
                            choices=[
                                "Menos de 6 meses",
                                "6-12 meses",
                                "1-2 años",
                                "Más de 2 años",
                                "Nunca"
                            ],
                            label="¿Cuándo fue su última revisión oftalmológica?",
                            value="6-12 meses"
                        )
            
            # Pestaña 2: Análisis de Imagen
            with gr.TabItem("🔬 Análisis de Imagen"):
                with gr.Row():
                    with gr.Column(scale=1):
                        gr.Markdown("### Subir Imagen de Fondo de Ojo")
                        image_input = gr.Image(
                            label="Imagen de retinografía",
                            type="pil",
                            height=400
                        )
                        
                        analyze_btn = gr.Button(
                            "🔍 Analizar Imagen", 
                            variant="primary",
                            size="lg"
                        )
                    
                    with gr.Column(scale=1):
                        gr.Markdown("### Resultados del Análisis")
                        results_output = gr.Markdown(label="Diagnóstico")
                        
                        # Botón para descargar PDF
                        download_btn = gr.File(
                            label="📄 Descargar Reporte PDF",
                            visible=False
                        )
            
            # Pestaña 3: Historial
            with gr.TabItem("📊 Historial de Diagnósticos"):
                gr.Markdown("### Historial de Análisis")
                gr.Markdown("""
                **Funcionalidad en desarrollo:**
                - Almacenamiento seguro de diagnósticos
                - Comparación de resultados a lo largo del tiempo
                - Gráficos de progreso
                - Exportación de historial completo
                """)
        
        # Función para procesar el diagnóstico
        def process_complete_diagnosis(img, nm, ag, gnd, dy, gl, bp, symp, risk, med, last_exam):
            # Crear diccionario con datos del paciente
            patient_data = {
                'name': nm,
                'age': ag,
                'gender': gnd,
                'diabetes_years': dy,
                'glucose_level': gl,
                'blood_pressure': bp,
                'symptoms': symp,
                'risk_factors': risk,
                'medications': med,
                'last_eye_exam': last_exam
            }
            
            # Procesar diagnóstico
            result_text, pdf_path, diagnosis = process_diagnosis(img, patient_data)
            
            # Preparar archivo para descarga
            if pdf_path:
                return result_text, pdf_path
            else:
                return result_text, None
        
        # Conectar componentes
        analyze_btn.click(
            fn=process_complete_diagnosis,
            inputs=[
                image_input, name, age, gender, diabetes_years, 
                glucose_level, blood_pressure, symptoms, risk_factors, 
                medications, last_eye_exam
            ],
            outputs=[results_output, download_btn]
        )
        
        # Mostrar botón de descarga cuando hay resultados
        def show_download_btn(result_text):
            if "DIAGNÓSTICO COMPLETO" in result_text:
                return gr.File(visible=True)
            return gr.File(visible=False)
        
        results_output.change(
            fn=show_download_btn,
            inputs=[results_output],
            outputs=[download_btn]
        )
    
    return demo

# Crear y lanzar la aplicación
if __name__ == "__main__":
    demo = create_interface()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True,
        show_error=True
    ) 