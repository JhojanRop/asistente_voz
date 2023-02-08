import speech_recognition as sr
import yfinance as yf
import pyttsx3, pywhatkit, pyjokes, webbrowser, wikipedia
import datetime

#? Utilidades
def ver_voces():
  engine = pyttsx3.init()
  for voz in engine.getProperty('voices'):
    print(voz)

#! Audio a texto
def transformar_audio():
  r = sr.Recognizer()
  with sr.Microphone() as origen:
    # Tiempo de espera
    r.pause_threshold = .8
    # Comienzo
    print('Microfono listo')
    audio = r.listen(origen)

    try:
      pedido = r.recognize_google(audio, language='es-co')
      print(pedido)
      return pedido
    except sr.UnknownValueError:
      print('--- Value Error ---\nNo entendi')
      return 'Error'
    except sr.RequestError:
      print('--- Request Error ---\nNo hay servicio')
      return 'Error'
    except:
      print('--- Unknown Error ---\nError desconocido')
      return 'Error'

#! Voces
voces = {
  'sabina':'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0',

  'zira':'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0',

  'david':'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0',

  'helena':'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0',
}

#! Texto a voz
def hablar(mensaje):
  engine = pyttsx3.init()
  engine.setProperty('voice', voces['sabina'])
  engine.say(mensaje)
  engine.runAndWait()

#! Informar dia
def dia():
  dia = datetime.date.today()
  dia_semana = dia.weekday()
  calendario = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
  
  hablar(f'Hoy es {calendario[dia_semana]}')

#! Informar hora
def hora():
  hora = datetime.datetime.now()
  print(hora)

  hora = f'En este momento son las {hora.hour if hora.hour <= 12 else (hora.hour-12)} y {hora.minute} de {"la noche" if hora.hour >= 18 else ("la mañana" if hora.hour < 12 else ("el medio día" if hora.hour in range(12,13) else ()))}'
  hablar(hora)

#! Saludo inicial
def saludo():
  hablar(f'{"Buenos días" if datetime.datetime.now().hour < 12 else ("Buenas tardes" if datetime.datetime.now().hour > 11 and datetime.datetime.now().hour < 7 else "Buenas noches")} Yojan, ¿En qué te puedo ayudar?')

#! Funcion central
def pedidos():
  saludo()

  while True:
    pedido = transformar_audio().lower()

    if 'qué hora es' in pedido:
      hora()
    elif 'qué dia es' in pedido:
      dia()
    elif 'apaga te' in pedido:
      hablar('Fué un placer atenderte')
      break
    elif 'abre youtube' in pedido:
      hablar('Abriendo YouTube')
      webbrowser.open('https://www.youtube.com')
    elif 'abre el navegador' in pedido:
      hablar('Abriendo el navegador')
      webbrowser.open('https://www.google.com')

pedidos()