#!/usr/bin/env python3
"""
Script para generar datos de demostración realistas para SightTech
Genera pacientes y diagnósticos con datos médicos plausibles
"""

import random
import json
from datetime import datetime, timedelta
from app import app, db, Patient, Diagnosis

# Nombres realistas para pacientes
NOMBRES_MASCULINOS = [
    "Carlos Mendoza", "Roberto Silva", "Miguel Torres", "José García", "Luis Rodríguez",
    "Fernando López", "Antonio Martínez", "Ricardo Pérez", "Eduardo González", "Manuel Ruiz",
    "Francisco Morales", "Alberto Jiménez", "Diego Castro", "Sergio Vargas", "Rafael Herrera"
]

NOMBRES_FEMENINOS = [
    "María González", "Ana López", "Carmen Rodríguez", "Isabel Martínez", "Rosa Pérez",
    "Elena García", "Patricia Silva", "Monica Torres", "Laura Castro", "Sofia Vargas",
    "Claudia Morales", "Verónica Jiménez", "Adriana Herrera", "Gabriela Ruiz", "Daniela Mendoza"
]

# Medicamentos comunes
MEDICAMENTOS = [
    "Metformina 500mg 2x día",
    "Metformina 850mg 2x día",
    "Glimepirida 1mg 1x día",
    "Glimepirida 2mg 1x día",
    "Insulina NPH 20 unidades",
    "Insulina Regular 10 unidades",
    "Losartán 50mg 1x día",
    "Amlodipino 5mg 1x día",
    "Atorvastatina 20mg 1x día",
    "Metformina 500mg 2x día, Glimepirida 1mg 1x día",
    "Metformina 850mg 2x día, Losartán 50mg 1x día",
    "Insulina NPH 25 unidades, Metformina 500mg 2x día"
]

# Comorbilidades
COMORBILIDADES = [
    "Hipertensión arterial",
    "Dislipidemia",
    "Obesidad",
    "Enfermedad renal crónica",
    "Hipertensión arterial, dislipidemia",
    "Obesidad, hipertensión arterial",
    "Enfermedad renal crónica, hipertensión arterial",
    "Dislipidemia, obesidad",
    "Hipertensión arterial, dislipidemia, obesidad",
    "Ninguna"
]

def generar_paciente():
    """Genera un paciente con datos médicos realistas"""
    
    # Género y nombre
    genero = random.choice(["Masculino", "Femenino"])
    if genero == "Masculino":
        nombre = random.choice(NOMBRES_MASCULINOS)
    else:
        nombre = random.choice(NOMBRES_FEMENINOS)
    
    # Edad (mayormente adultos mayores con diabetes)
    edad = random.randint(45, 75)
    
    # Años con diabetes (correlacionado con edad)
    anos_diabetes = random.randint(1, min(edad - 20, 25))
    
    # Tipo de diabetes (mayormente tipo 2)
    tipo_diabetes = random.choices(
        ["tipo_1", "tipo_2", "gestacional", "prediabetes"],
        weights=[0.15, 0.7, 0.1, 0.05]
    )[0]
    
    # Glucosa (correlacionada con control)
    glucosa = random.randint(120, 280)
    
    # HbA1c (correlacionada con glucosa)
    hba1c = round(random.uniform(6.0, 12.0), 1)
    
    # Presión arterial
    sistolica = random.randint(110, 180)
    diastolica = random.randint(70, 110)
    presion = f"{sistolica}/{diastolica}"
    
    # Colesterol
    colesterol = random.randint(150, 350)
    
    # IMC
    imc = round(random.uniform(22.0, 38.0), 1)
    
    # Capacidad visual (correlacionada con severidad)
    vision_od = random.choice(["20/20", "20/25", "20/30", "20/40", "20/50", "20/60", "20/70", "20/80"])
    vision_oi = random.choice(["20/20", "20/25", "20/30", "20/40", "20/50", "20/60", "20/70", "20/80"])
    
    # Medicamentos
    medicamentos = random.choice(MEDICAMENTOS)
    
    # Comorbilidades
    comorbilidades = random.choice(COMORBILIDADES)
    
    # Último examen ocular
    ultimo_examen = random.choices(
        ["menos_6_meses", "6_12_meses", "1_2_anos", "mas_2_anos", "nunca"],
        weights=[0.3, 0.4, 0.2, 0.08, 0.02]
    )[0]
    
    # Diagnóstico previo
    diagnostico_previo = random.choices(
        ["ninguno", "leve", "moderado", "severo", "proliferativo"],
        weights=[0.4, 0.3, 0.2, 0.08, 0.02]
    )[0]
    
    return {
        "name": nombre,
        "age": edad,
        "gender": genero,
        "diabetes_years": anos_diabetes,
        "diabetes_type": tipo_diabetes,
        "glucose_level": glucosa,
        "hba1c": hba1c,
        "blood_pressure": presion,
        "cholesterol": colesterol,
        "bmi": imc,
        "vision_right_eye": vision_od,
        "vision_left_eye": vision_oi,
        "medications": medicamentos,
        "comorbidities": comorbilidades,
        "last_eye_exam": ultimo_examen,
        "previous_diagnosis": diagnostico_previo
    }

def generar_diagnostico(paciente):
    """Genera un diagnóstico basado en los datos del paciente"""
    
    # Calcular riesgo basado en datos del paciente
    riesgo = 0
    
    # Edad
    if paciente["age"] > 70: riesgo += 3
    elif paciente["age"] > 60: riesgo += 2
    elif paciente["age"] > 50: riesgo += 1
    
    # HbA1c
    if paciente["hba1c"] > 9.0: riesgo += 3
    elif paciente["hba1c"] > 8.0: riesgo += 2
    elif paciente["hba1c"] > 7.0: riesgo += 1
    
    # Años con diabetes
    if paciente["diabetes_years"] > 15: riesgo += 2
    elif paciente["diabetes_years"] > 10: riesgo += 1
    
    # Presión arterial
    sistolica = int(paciente["blood_pressure"].split("/")[0])
    if sistolica > 160: riesgo += 2
    elif sistolica > 140: riesgo += 1
    
    # Determinar diagnóstico basado en riesgo
    if riesgo >= 8:
        diagnostico = "Retinopatía diabética proliferativa (PDR)"
        severidad = 4
        confianza = random.uniform(85, 95)
    elif riesgo >= 6:
        diagnostico = "Retinopatía diabética severa (NPDR)"
        severidad = 3
        confianza = random.uniform(80, 90)
    elif riesgo >= 4:
        diagnostico = "Retinopatía diabética moderada (NPDR)"
        severidad = 2
        confianza = random.uniform(75, 85)
    elif riesgo >= 2:
        diagnostico = "Retinopatía diabética leve (NPDR)"
        severidad = 1
        confianza = random.uniform(70, 80)
    else:
        diagnostico = "Sin retinopatía diabética"
        severidad = 0
        confianza = random.uniform(85, 95)
    
    return {
        "prediction": diagnostico,
        "confidence": round(confianza, 1),
        "severity": severidad
    }

def generar_datos_demo(num_pacientes=20):
    """Genera datos de demostración completos"""
    
    with app.app_context():
        # Inicializar base de datos
        print("🗄️ Inicializando base de datos...")
        db.drop_all()
        db.create_all()
        print("✅ Base de datos inicializada")
        
        print(f"🎯 Generando {num_pacientes} pacientes de demostración...")
        
        pacientes_creados = []
        
        for i in range(num_pacientes):
            # Generar paciente
            datos_paciente = generar_paciente()
            
            # Crear paciente en BD
            paciente = Patient(**datos_paciente)
            db.session.add(paciente)
            db.session.commit()
            
            # Generar 1-3 diagnósticos por paciente
            num_diagnosticos = random.randint(1, 3)
            
            for j in range(num_diagnosticos):
                # Generar diagnóstico
                datos_diagnostico = generar_diagnostico(datos_paciente)
                
                # Fecha del diagnóstico (últimos 6 meses)
                fecha = datetime.now() - timedelta(
                    days=random.randint(0, 180),
                    hours=random.randint(0, 23),
                    minutes=random.randint(0, 59)
                )
                
                # Crear diagnóstico
                diagnostico = Diagnosis(
                    patient_id=paciente.id,
                    image_paths=json.dumps([f"demo_image_{i}_{j}.jpg"]),
                    prediction=datos_diagnostico["prediction"],
                    confidence=datos_diagnostico["confidence"],
                    severity=datos_diagnostico["severity"],
                    recommendations=json.dumps([
                        "Control estricto de la glucosa en sangre",
                        "Revisiones oftalmológicas regulares",
                        "Mantener presión arterial controlada"
                    ]),
                    symptoms=json.dumps(["vision_borrosa", "manchas_negras"]),
                    medical_history=json.dumps(datos_paciente),
                    created_at=fecha
                )
                
                db.session.add(diagnostico)
            
            db.session.commit()
            pacientes_creados.append(paciente)
            
            print(f"✅ Paciente {i+1}/{num_pacientes}: {paciente.name} ({paciente.age} años)")
        
        print(f"\n🎉 ¡Datos de demostración generados exitosamente!")
        print(f"📊 Total de pacientes: {len(pacientes_creados)}")
        
        # Mostrar estadísticas
        total_diagnosticos = Diagnosis.query.count()
        print(f"📋 Total de diagnósticos: {total_diagnosticos}")
        
        # Distribución por severidad
        for i in range(5):
            count = Diagnosis.query.filter_by(severity=i).count()
            print(f"   Nivel {i}: {count} diagnósticos")
        
        return pacientes_creados

if __name__ == "__main__":
    print("🚀 Iniciando generación de datos de demostración...")
    print("=" * 50)
    
    try:
        pacientes = generar_datos_demo(25)  # Generar 25 pacientes
        print("\n✅ ¡Proceso completado exitosamente!")
        print("🌐 Puedes acceder al dashboard para ver los datos generados.")
        
    except Exception as e:
        print(f"❌ Error generando datos: {e}")
        import traceback
        traceback.print_exc() 