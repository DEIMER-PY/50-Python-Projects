# Install speechRecognition with pip install SpeechRecognition
# Install pyttsx3 with pip install pyttsx3

# https://www.amazon.es/s?k=

import speech_recognition as sr
import webbrowser
import pyttsx3

# Inicialización de componentes
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def talk():
    """Escucha el micrófono y devuelve el texto reconocido."""
    mic = sr.Microphone()
    with mic as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
        
    try:
        # Reconocimiento de voz usando Google
        text = recognizer.recognize_google(audio, language='es-ES')
        print(f"Has dicho: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("No te he entendido.")
        return ""
    except sr.RequestError:
        print("Error en el servicio de reconocimiento.")
        return ""

def speak(text):
    """Hace que el asistente hable."""
    engine.say(text)
    engine.runAndWait()

# Lógica principal del proyecto
if __name__ == "__main__":
    print("Iniciando asistente... di 'amazon' para buscar.")
    
    # Aquí capturamos la primera entrada
    user_input = talk()
    
    if 'amazon' in user_input:
        speak('¿Qué quieres comprar en Amazon?')
        producto = talk()
        if producto:
            url = f'https://www.amazon.es/s?k={producto}'
            webbrowser.open(url)
            speak(f'Buscando {producto} en Amazon')

