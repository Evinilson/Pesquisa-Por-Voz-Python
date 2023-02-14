import speech_recognition as sr

# Cria um objeto de reconhecimento de fala
microfone = sr.Recognizer()

def reconhecer_fala():
    try:
        # Usa o microfone como fonte de áudio
        with sr.Microphone() as source:
            print("Fale algo...")
            # Ajusta o nível de ruído de fundo do microfone para uma melhor transcrição
            microfone.adjust_for_ambient_noise(source)
            # Captura o áudio
            audio = microfone.listen(source)
        # Transcreve o áudio em texto usando o Google Speech Recognition
        texto = microfone.recognize_google(audio, language='pt-PT')
        return texto
    except sr.UnknownValueError:
        print("Não foi possível transcrever o áudio")
    except sr.RequestError as e:
        print("Erro ao conectar-se ao serviço de reconhecimento de fala: {0}".format(e))

def main():
    print("Este é um programa de pesquisa por voz. Por favor, fale o que deseja pesquisar.")
    texto_transcrito = reconhecer_fala()
    if texto_transcrito is not None:
        print(f"Você disse: {texto_transcrito}")

main()
