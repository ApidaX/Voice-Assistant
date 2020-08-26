# Importing all the neccessary modules
import pyttsx3
import speech_recognition as sr
import os

# Speaking the text 
def speak(speak):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.getProperty('rate')
    engine.setProperty('rate', 155)
    engine.say(speak)
    engine.runAndWait()

listen = True
a = 1

while listen != "stop":

    if a == 1:
        print("Hi there, I'm your personal assistant. Write or speak what you want me to do for you :)")
        speak("Hi there, I'm your personal assistant. Write or speak what you want me to do for you")

    # Recognising speech
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    print("Recognizing...")
    listen = r.recognize_google(audio)
    listen.lower()
    print(f"You Said: {listen}")
    
    if "command prompt" in listen:
        print("Opening Command Prompt")
        speak("Opening Command Prompt")
        
        os.startfile(os.path.join("C:\Windows\system32\cmd.exe"))

    a += 1