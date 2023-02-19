import speech_recognition as sr
from gtts import gTTS
import pygame as pg
import os


#Função para reprodução da fala
def falar(texto: str):
    # Criar o objeto gTTS para traduzir o texto     
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
    

# Função para reconecimento da fala
def reconhecer_fala() -> str:
    while True:    
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
            return microfone.recognize_google(audio, language='pt-PT').lower()
        
        except sr.UnknownValueError:
            # Mensagem de erro
            falar("Não foi possível transcrever o áudio, fala novamente")
            


# Função para confimar a fala
def confirmar_fala():
    while True:
        resposta = reconhecer_fala()
        texto = "Você disse: " + resposta
        falar(texto)
        falar("Diga Sim ou Não para confimar")
        confirmacao = reconhecer_fala()
        if confirmacao[0] == "s":
            return resposta
        else:
            falar(f"A sua resposta foi entendida como: {confirmacao}")
            falar(f"Fale novamente")        
            

# Função para descrever o projeto
def descricao():
    # Discrição do controlador
    falar("Como podes ver, existe um controlador de resposta onde é confirmada suas respostas antes de serem executadas. Para desativar, diga desativar, caso a sua resposta for diferente de desativar ele continuará ativo")

    # Controlador de fala
    controlador = True
    if confirmar_fala() == "desativar":
        controlador = False

    # Os navegadores do aplicativo
    falar("Este aplicativo é um projeto onde apenas com o voz podes fazer pesquisas num navegador, por padrão ele está configurado para utilizar o navegador Chrome.")
    
    # Como abrir o navegador
    falar("Para abrir o Chrome, podes dizer abra o Chrome, abra o navegador ou abra o browser. Também é possível abrir o firefox dizendo abra o firefox.")
    
    # Como ter uma melhor captura do áudio
    falar("Para um melhor desempenho na captura da voz espere uns 2 segundos antes da falar algo.")
    
    # como pesquisar
    falar("Após o seu navegador estiver aberto você só precisa dizer o que você precisa pesquisar.")
    
    # Exemplo de pesquisas 
    return controlador
 
    
# O main do projeto
def main():
    # Controlador de confirmação de fala por padrão ativado
    controlador = True
    
    # Mensagem de introdução
    falar("Este é um programa de pesquisa por voz.")
    
    # Saber mais do projeto
    falar("Para saber mais sobre este projeto, diga projeto.")
    if "projeto" == confirmar_fala():
        controlador = descricao()
    
    # Escolha do navegador
    falar("Diga abra o fireFox ou continuar para abrir o navegador")
    if controlador:
        resposta = confirmar_fala()
    else:
        resposta = reconhecer_fala()
    
    # Abrir o navegador
    if resposta in ["abra o chrome", "abra o navegador", "abra o browser", "continuar"] :
        os.system("start chrome")
    elif resposta == "abra o firefox":
        os.system("start firefox")
    else:
        falar("Não foi possível identificar o navegador que pretende abrir. Por padrão será aberta o chrome.")
        os.system("star chrome")
        
    
    # Capturar a pesquisa 
    falar("O que desejas pesquisar?")
    if controlador:
        resposta = confirmar_fala()
    else:
        resposta = reconhecer_fala()
        


# Execução do programa
main()
