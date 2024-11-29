import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises...Please wait")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me anything...')
        recorded_audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(recorded_audio, language='en_US')
        text = text.lower()
        print('Your message:', format(text))
        
        if 'chrome' in text:
            a = 'Opening Chrome...'
            engine.say(a)
            engine.runAndWait()
            program_name = "C:/Program Files/Google/Chrome/Application/chrome.exe"
            subprocess.Popen([program_name])
        
        elif 'time' in text:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            print(current_time)
            engine.say(current_time)
            engine.runAndWait()
        
        elif 'play' in text:
            a = 'Opening YouTube...'
            engine.say(a)
            engine.runAndWait()
            pywhatkit.playonyt(text)
        
        elif 'youtube' in text:
            b = 'Opening YouTube...'
            engine.say(b)
            engine.runAndWait()
            webbrowser.open('http://www.youtube.com')

        elif 'google' in text:
            c ='opening google...'
            engine.say(c)
            engine.runAndWait()
            webbrowser.open('http://www.google.com')

        elif 'linkedin profile' in text:
            d='azardeen linkedin profile...'
            engine.say(d)
            engine.runAndWait()
            webbrowser.open('https://in.linkedin.com/in/mohamed-azardeen-564b8029b')

        elif 'github' in text:
            e='azardeen github profile...'
            engine.say(e)
            engine.runAndWait()
            webbrowser.open('https://github.com/Azar7867')
            
    except Exception as ex:
        print(ex)

while True:
    cmd()
