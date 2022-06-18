import requests
import webbrowser
import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime
from random import choice
from pprint import pprint

from functions.online_ops import find_my_ip, play_on_youtube, search_on_google, search_on_wikipedia, send_whatsapp_message
from functions.offline_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord
from utils import opening_text


USERNAME = config('USER')
BOTNAME = config('BOTNAME')

# Initialize the speech engine
engine = pyttsx3.init('sapi5') # driverName on Windows, Microsoft Speech API.

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Male)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()


# Greet the user
def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")


# Takes Input from User
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-us')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night Ibtihel, take care!")
            else:
                speak('Have a good day Cutie!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            open_notepad()

        elif 'open discord' in query:
            open_discord()

        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'open calculator' in query:
            open_calculator()

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen Madam.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, Madam?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen Madam.")
            print(results)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, Madam?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'social media' in query:
            speak('Which platform or website do you want me to open, Madam?')
            page = take_user_input().lower()
            webbrowser.open_new_tab(f"https://{page}.com")

        elif 'search on google' in query:
            speak('What do you want to search on Google, Madam?')
            query = take_user_input().lower()
            search_on_google(query)
            
        elif 'search location' in query:
            speak('What location you want to search, Madam?')
            location = take_user_input()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.open_new_tab(url)
            speak('Here is the location ' + location)

        elif "send whatsapp message" in query:
            speak(
                'On what number should I send the message Madam? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message Madam?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message Madam.")
            
        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f'Madam, the time is {strTime}')
        
