# DeepLog: detección de incidentes mediante el uso de LLMs

Este proyecto utiliza IA (Llama 3) para analizar logs de sistema y detectar ataques de ciberseguridad en tiempo real.

## Características actuales
- **Análisis automatizado:** lectura de archivos de logs (`access.log`).
- **IA local:** integración con Ollama para procesar datos de forma privada.
- **Salida estructurada:** generación de respuestas en formato JSON para facilitar la automatización.
- **Detección de amenazas:** especializado en identificar ataques de fuerza bruta.

## Tecnologías utilizadas
- Python 3.14.3
- Ollama (modelo Llama 3)
- LangChain (community)
- Git para control de versiones

## Próximos pasos
- Implementar monitoreo en tiempo real (Live Tail).
- Ampliar la detección a ataques de Inyección SQL.
- Crear un Dashboard básico para visualizar las alertas.