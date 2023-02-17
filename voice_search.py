import speech_recognition as sr
from gtts import gTTS
import pygame as pg
import os


#Função para reprodução da fala
def reproduzir_fala(texto: str):
    # Criar o objeto gTTS para traduir o texto     
    tts = gTTS(text=texto, lang="pt-pt")
    
    # Transformar o texto para o formato mp3
    tts.save("fala.mp3")
    
    # Inicializa a biblioteca Pygame
    pg.init()

    # Carrega o arquivo mp3
    pg.mixer.music.load("fala.mp3")

    # Inicia a reprodução do áudio
    pg.mixer.music.play()

    # Espera a reprodução terminar
    while pg.mixer.music.get_busy():
        pg.time.Clock().tick(10)

    # Finaliza a biblioteca Pygame
    pg.quit()
    
    # Apaga o arquivo fala.mp3
    os.remove("fala.mp3")
    

# Fubção para reconecimento da fala
def reconhecer_fala() -> str:    
    try:
        # Criação do objeto de reconhecimento de fala
        microfone = sr.Recognizer()
        
        # Uso do microfone como fonte de áudio
        with sr.Microphone() as mic:
            # Ajusta o nível de ruído de fundo do microfone para uma melhor transcrição
            microfone.adjust_for_ambient_noise(mic)
            
            # Captura o áudio
            audio = microfone.listen(mic)
            
        # Transcreve o áudio em texto usando o Google Speech Recognition
        return microfone.recognize_google(audio, language='pt-PT')
    
    except sr.UnknownValueError:
        # Mensagem de erro
        reproduzir_fala("Não foi possível transcrever o áudio")


# O main do projeto
def main():
    # Mensagem de introdução
    reproduzir_fala("Este é um programa de pesquisa por voz.")
    

# Execução do programa
main()
