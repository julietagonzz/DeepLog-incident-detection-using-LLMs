import ollama
import json

def leer_logs(nombre_archivo):
    # 1. leemos el archivo
    with open(nombre_archivo, 'r') as logs:
        return logs.read()


def analizar_con_ia(contenido):
    # 2. configuramos la consulta a la IA con ese contenido que hemos leido del archivo
    prompt = f"Actúa como un experto en ciberseguridad. Analiza los siguientes logs y dime si ves algún ataque de fuerza bruta. RESPONDE SIEMPRE EN ESPAÑOL Y ÚNICAMENTE en formato JSON con estas claves: 'ip_atacante', 'nivel_riesgo' y 'resumen'. Asegúrate de que 'nivel_riesgo' sea siempre una CADENA DE TEXTO (ej: 'alto', 'medio', 'bajo') y nunca un número. No añadas saludos ni explicaciones extra:\n\n{contenido}"

    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])

    # 3. imprimimos la respuesta de la IA
    print("\nResultado del análisis:")
    print(response['message']['content'])
    return json.loads(response['message']['content'])


def ejecutar_accion(response):
    # 4. ahora, como tenemos la respuesta en JSON, la parseamos para poder usarla en nuestro código
    print(f"ALERTA DETECTADA: se ha identificado la IP {response['ip_atacante']}")
    print(f"Procediendo a registrar el incidente con riesgo: {response['nivel_riesgo'].upper()}")

    # En lugar de solo imprimir, vamos a tomar una decisión lógica:
    riesgo = str(response.get('nivel_riesgo')).lower() # get es mas seguro por que si la clave no existe devuelve None
    
    if riesgo == "alto":
        print("!!! BLOQUEO AUTOMÁTICO ACTIVADO !!!")
    else:
        print("Monitoreando actividad...")

if __name__ == "__main__":
    nombre_archivo = 'access.log'
    contenido = leer_logs(nombre_archivo)
    print("--- Analizando los logs, espera un momento... ---")

    try:
        response = analizar_con_ia(contenido)
        ejecutar_accion(response)
    except Exception as e:
        print(f"Error al analizar los logs: {e}")