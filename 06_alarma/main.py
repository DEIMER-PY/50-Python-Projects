import os
import time
from playsound import playsound

def alarm(minutes, seconds):
    # Usar os.path.dirname(__file__) asegura que el script encuentre el MP3
    # siempre que esté en la misma carpeta que el archivo .py
    folder = os.path.dirname(__file__)
    sound_path = os.path.join(folder, "alarma_python.mp3")

    # Validación de existencia del archivo
    if not os.path.exists(sound_path):
        print(f"Error: No se encuentra el archivo {sound_path}")
        return

    total_seconds = minutes * 60 + seconds
    print(f"La alarma sonará en {minutes} minutos y {seconds} segundos.")
    print("Esperando...")

    # El programa se suspende, ahorrando CPU
    time.sleep(total_seconds)

    print("¡TIEMPO AGOTADO!")
    try:
        playsound(sound_path)
    except Exception as e:
        print(f"Error al reproducir el sonido: {e}")

if __name__ == "__main__":
    # Captura de datos del usuario
    try:
        m = int(input("Ingresa los minutos de la alarma: "))
        s = int(input("Ingresa los segundos de la alarma: "))
        alarm(m, s)
    except ValueError:
        print("Por favor, ingresa números enteros válidos.")

