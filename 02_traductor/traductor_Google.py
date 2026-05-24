from deep_translator import GoogleTranslator

def traducir_texto():
    texto_a_traducir = input('¿Qué quieres traducir? ')
    
    try:
        # Usamos GoogleTranslator, que es muy estable
        resultado = GoogleTranslator(source='es', target='en').translate(texto_a_traducir)
        
        print(f"Traducción: {resultado}")
    except Exception as e:
        print(f"Error en la traducción: {e}")

if __name__ == "__main__":
    traducir_texto()