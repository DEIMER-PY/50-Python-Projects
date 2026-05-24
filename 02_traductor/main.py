from translate import Translator

def traducir_texto():
    try:
        # Configuración del traductor (español a inglés)
        translator = Translator(from_lang='spanish', to_lang='english')
        
        # Entrada del usuario
        texto_a_traducir = input('¿Qué quieres traducir? ')
        
        # Proceso de traducción
        print("Traduciendo...")
        resultado = translator.translate(texto_a_traducir)
        
        # Salida
        print(f"Traducción: {resultado}")
        
    except Exception as e:
        print(f"Ocurrió un error al traducir: {e}")

if __name__ == "__main__":
    traducir_texto()