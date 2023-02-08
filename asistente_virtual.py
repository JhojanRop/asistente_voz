import speech_recognition as sr
import yfinance as yf
import pyttsx3, pywhatkit, pyjokes, webbrowser, wikipedia
import datetime

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

  'david':'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
}

#! Texto a voz
def hablar(mensaje):
  engine = pyttsx3.init()
  # engine.setProperty('voice', voces['sabina'])
  # engine.setProperty('voice', voces['david'])
  engine.setProperty('voice', voces['zira'])
  engine.say(mensaje)
  engine.runAndWait()

hablar('Buenas noches, Jhojan')

# engine = pyttsx3.init()
# for voz in engine.getProperty('voices'):
#   print(voz)
