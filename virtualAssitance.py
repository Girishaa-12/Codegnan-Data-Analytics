import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except Exception:
        print("Sorry, please say that again.")
        return ""


def wish_user():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning. I am your virtual assistant. How can I help you?")

    elif hour < 18:
        speak("Good Afternoon. I am your virtual assistant. How can I help you?")

    else:
        speak("Good Evening. I am your virtual assistant. How can I help you?")

speak("I am your virtual assistant")

wish_user()

while True:

    command = take_command()

    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, sentences=2)
        print(info)
        speak(info)

    elif "exit" in command:
        speak("Goodbye")
        break



    
    
    
