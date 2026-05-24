from googletrans import Translator

def traducir_texto():
    # Inicializamos el traductor
    translator = Translator()
    
    texto_a_traducir = input('¿Qué quieres traducir? ')
    
    try:
        # Detectamos y traducimos a inglés
        resultado = translator.translate(texto_a_traducir, src='es', dest='en')
        
        print(f"Traducción: {resultado.text}")
    except Exception as e:
        print(f"Error en la traducción: {e}")

if __name__ == "__main__":
    traducir_texto()