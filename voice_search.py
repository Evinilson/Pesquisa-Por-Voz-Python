import speech_recognition as sr
from gtts import gTTS
from playsound import playsound





def reproduzir_fala(texto: str):
    tts = gTTS(text=texto, lang='pt-br')
    tts.save('audio.mp3')
    playsound('audio.mp3')


def reconhecer_fala():
    # Cria um objeto de reconhecimento de fala
    microfone = sr.Recognizer()
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


def confirme_fala():
    while True:
        fala = reconhecer_fala()
        if fala is not None:
            frase = f"Você disse: {fala}"
            reproduzir_fala(frase)
            
        if 0 == 1:
            break
    
    
    
def main():
    print("Este é um programa de pesquisa por voz. Por favor, fale o que deseja pesquisar.")
    texto_transcrito = confirme_fala()
    print(texto_transcrito)


main()
