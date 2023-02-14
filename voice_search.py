import speech_recognition as sr

# Cria um objeto de reconhecimento de fala
r = sr.Recognizer()

# Usa o microfone como fonte de áudio
with sr.Microphone() as source:
    print("Fale algo...")
    # Ajusta o nível de ruído de fundo do microfone para uma melhor transcrição
    r.adjust_for_ambient_noise(source)
    # Captura o áudio
    audio = r.listen(source)

# Transcreve o áudio em texto usando o Google Speech Recognition
try:
    text = r.recognize_google(audio, language='pt-BR')
    print("Você disse: ", text)
except sr.UnknownValueError:
    print("Não foi possível transcrever o áudio")
except sr.RequestError as e:
    print("Erro ao conectar-se ao serviço de reconhecimento de fala: {0}".format(e))
