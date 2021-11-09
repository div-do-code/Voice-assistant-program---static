import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import pyjokes
from niftystocks import ns
from nsetools import Nse
from wikipedia.wikipedia import search


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('Hello I am Aunty, a voice assistant coded by Divyanshu, HAHA, lets be true, he took code from github and stackover flow')
talk('well you can ask me some questions, just like you ask to your pados wali aunty')


def take_command():
    try:
        with sr.Microphone() as source:
             print('I m Listening...')
             voice = listener.listen(source)
             command = listener.recognize_google(voice)
             # Making the word aunty mandatory.
             # # Otherwise it won't listen.. The name should be call only aunty.
             command = command.lower()
             if 'aunty' in command:
                command = command.replace('aunty', '')
                print(command)
                


    except:
       pass
    return command

def speak_aunty():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing'+ song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)


    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person,1)
        talk(info)
        print(info)

    elif 'what is' in command:
        asked = command.replace('what is', '')
        info = wikipedia.summary(asked,1)
        talk(info)
        print(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(talk)   
    
    elif 'nifty' in command:
        nse = Nse()
        talk('There are total fifty stocks in nifty fifty')
        # talk(ns.get_nifty50())
        talk(nse.get_index_quote('NIFTY 50'))
        print(talk)
    
    elif 'marry' in command:
        talk('which friend?') 
        talk('')
        talk('')
        talk('')
        talk('')
        talk('')
        talk('')
        talk('')
        talk('')
        talk('')
        talk('')
        talk('')
        talk('')
        talk('')
        talk('')
        talk('')
        talk('tell him pehli fursat Mein nikkal')
        print(talk)
    
    # elif 'siri' in command:
    #     sensex_point = nifpy.get_sensex()
    #     #talk('tell him Pehli Fursat Mai Nikal')
    #     talk(sensex_point)
    #     print('playing')

while True:
    speak_aunty()        



