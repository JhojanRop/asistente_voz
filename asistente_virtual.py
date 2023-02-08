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

transformar_audio()