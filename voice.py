import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()

    except Exception:
        return ""

while True:

    command = take_command()

    if command == "":
        speak("I did not understand. Please speak again.")
        continue

    hour = datetime.datetime.now().hour

    # Morning
    if "good morning" in command or "morning" in command:

        if hour < 12:
ss            speak(f"Good Morning! Current hour is {hour}")
        elif hour < 18:
            speak(f"It is not morning. Current hour is {hour}. It is Good Afternoon.")
        else:
            speak(f"It is not morning. Current hour is {hour}. It is Good Evening.")

    # Afternoon
    elif "good afternoon" in command or "afternoon" in command:

        if 12 <= hour < 18:
            speak(f"Good Afternoon! Current hour is {hour}")
        elif hour < 12:
            speak(f"It is not afternoon. Current hour is {hour}. It is Good Morning.")
        else:
            speak(f"It is not afternoon. Current hour is {hour}. It is Good Evening.")

    # Evening
    elif "good evening" in command or "evening" in command:

        if hour >= 18:
            speak(f"Good Evening! Current hour is {hour}")
        elif hour < 12:
            speak(f"It is not evening. Current hour is {hour}. It is Good Morning.")
        else:
            speak(f"It is not evening. Current hour is {hour}. It is Good Afternoon.")

    # Exit
    elif "exit" in command:
        speak("Goodbye")
        break

    # Else block
    else:
        speak("Please say Good Morning, Good Afternoon, Good Evening, or Exit.")
