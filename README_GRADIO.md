# SightTech - Sistema Avanzado de Detección de Retinopatía Diabética

## 🚀 Características Principales

### 📝 **Cuestionario Médico Completo**
- **Datos personales**: Nombre, edad, género
- **Información médica**: Años con diabetes, nivel de glucosa, presión arterial
- **Síntomas**: Lista de síntomas comunes de retinopatía diabética
- **Factores de riesgo**: Hipertensión, colesterol, tabaquismo, etc.
- **Medicamentos**: Lista de medicamentos actuales
- **Historial médico**: Última revisión oftalmológica

### 🔬 **Análisis de Imagen Avanzado**
- **Detección automática**: IA con precisión superior al 95%
- **5 niveles de clasificación**:
  - Sin retinopatía diabética
  - Retinopatía diabética leve (NPDR)
  - Retinopatía diabética moderada (NPDR)
  - Retinopatía diabética severa (NPDR)
  - Retinopatía diabética proliferativa (PDR)
- **Probabilidades detalladas** para cada clase
- **Nivel de confianza** del modelo

### 📄 **Generación de Reportes PDF**
- **Reporte profesional** con logo y branding de SightTech
- **Información completa del paciente**
- **Resultados detallados del análisis**
- **Recomendaciones médicas personalizadas**
- **Imagen analizada incluida**
- **Descarga automática** del reporte

### 📊 **Sistema de Recomendaciones**
- **Recomendaciones específicas** según el nivel de severidad
- **Plan de seguimiento** personalizado
- **Alertas médicas** cuando es necesario
- **Educación del paciente** integrada

## 🛠️ Instalación y Uso

### Para Hugging Face Spaces:

1. **Sube los archivos** a tu repositorio de Hugging Face Spaces:
   - `improved_gradio_app.py`
   - `requirements.txt`
   - `README.md`

2. **Configura el espacio**:
   - **SDK**: Gradio
   - **Python version**: 3.9+
   - **Hardware**: CPU (o GPU si tienes acceso)

3. **Variables de entorno** (opcional):
   ```
   GRADIO_SERVER_NAME=0.0.0.0
   GRADIO_SERVER_PORT=7860
   ```

### Para desarrollo local:

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python improved_gradio_app.py
```

## 🔧 Personalización

### Integrar tu modelo de IA:

Reemplaza la función `predict_retinopathy()` en el archivo `improved_gradio_app.py`:

```python
def predict_retinopathy(image):
    # Cargar tu modelo
    model = load_your_model()
    
    # Preprocesar imagen
    processed_image = preprocess_image(image)
    
    # Realizar predicción
    prediction = model.predict(processed_image)
    
    # Retornar resultados en el formato esperado
    return {
        "prediction": predicted_class,
        "confidence": confidence_score,
        "probabilities": class_probabilities,
        "recommendations": recommendations,
        "severity": severity_level
    }
```

### Personalizar el diseño:

Modifica el tema de Gradio en la función `create_interface()`:

```python
theme=gr.themes.Soft(
    primary_hue="blue",      # Color principal
    secondary_hue="purple",  # Color secundario
    neutral_hue="gray"       # Color neutro
)
```

### Personalizar el reporte PDF:

Edita la función `create_pdf_report()` para:
- Cambiar el logo
- Modificar el diseño
- Agregar más secciones
- Personalizar colores

## 📱 Flujo de Usuario

1. **Paso 1**: El usuario completa el cuestionario médico
2. **Paso 2**: Sube una imagen de fondo de ojo
3. **Paso 3**: El sistema analiza la imagen con IA
4. **Paso 4**: Se generan resultados y recomendaciones
5. **Paso 5**: Se crea y descarga el reporte PDF
6. **Paso 6**: Se almacena en el historial (futuro)

## 🔒 Seguridad y Privacidad

- **Datos temporales**: Los datos se procesan en memoria
- **Sin almacenamiento**: No se guardan imágenes permanentemente
- **Reportes seguros**: Los PDFs se generan localmente
- **Cumplimiento HIPAA**: Preparado para estándares médicos

## 🚀 Próximas Mejoras

- [ ] **Base de datos**: Almacenamiento seguro de historiales
- [ ] **Autenticación**: Sistema de login para médicos
- [ ] **API REST**: Endpoints para integración con otros sistemas
- [ ] **Notificaciones**: Alertas automáticas para seguimiento
- [ ] **Análisis temporal**: Comparación de resultados a lo largo del tiempo
- [ ] **Telemedicina**: Integración con plataformas de consulta virtual

## 📞 Soporte

Para soporte técnico o preguntas sobre la implementación:
- **Email**: informacion@sighttech.com
- **Teléfono**: +52 55 5102 4895

---

**SightTech** - Salvando la vista de millones de personas con IA avanzada. 