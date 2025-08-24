#!/usr/bin/env python3
"""
Script para actualizar URLs cuando se tenga el dominio sighttech.mx
Ejecutar después de configurar el dominio en GoDaddy y Render
"""

import os
import re

def update_file(file_path, old_url, new_url):
    """Actualizar URLs en un archivo"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Contar ocurrencias
        count = content.count(old_url)
        if count > 0:
            # Reemplazar URLs
            new_content = content.replace(old_url, new_url)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ {file_path}: {count} URLs actualizadas")
            return True
        else:
            print(f"ℹ️  {file_path}: No se encontraron URLs para actualizar")
            return False
            
    except Exception as e:
        print(f"❌ Error actualizando {file_path}: {e}")
        return False

def main():
    """Función principal"""
    print("🌐 Actualizando URLs para dominio sighttech.mx")
    print("=" * 50)
    
    # URLs a actualizar
    updates = [
        # Backend URLs
        ('https://sighttech-backend.onrender.com', 'https://api.sighttech.mx'),
        
        # Frontend URLs en CORS
        ('https://sighttechfrontend.onrender.com', 'https://sighttech.mx'),
    ]
    
    # Archivos a actualizar
    files_to_update = [
        'backend/app.py',
        'app_analysis.html',
        'chatbot.js',
        'dashboard.html',
        'index.html',
        'render.yaml',
        'README_DEPLOY.md'
    ]
    
    total_updates = 0
    
    for old_url, new_url in updates:
        print(f"\n🔄 Actualizando: {old_url} → {new_url}")
        print("-" * 40)
        
        for file_path in files_to_update:
            if os.path.exists(file_path):
                if update_file(file_path, old_url, new_url):
                    total_updates += 1
            else:
                print(f"⚠️  {file_path}: Archivo no encontrado")
    
    print("\n" + "=" * 50)
    print(f"✅ Total de archivos actualizados: {total_updates}")
    print("\n📋 Próximos pasos:")
    print("1. Hacer commit y push de los cambios")
    print("2. Configurar DNS en GoDaddy")
    print("3. Configurar dominios personalizados en Render")
    print("4. Esperar propagación DNS (24-48 horas)")
    print("5. Probar la aplicación en sighttech.mx")

if __name__ == "__main__":
    main() 