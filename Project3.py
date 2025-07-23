import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os

# Initialize the voice engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I help you today?")

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio).lower()
            print("You said:", command)
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you please repeat?")
            return ""
        except sr.RequestError:
            speak("Sorry, there seems to be a network error.")
            return ""
        return command

def run_assistant():
    greet_user()
    while True:
        command = listen_command()

        if 'wikipedia' in command:
            topic = command.replace('wikipedia', '').strip()
            speak(f"Searching Wikipedia for {topic}")
            try:
                summary = wikipedia.summary(topic, sentences=2)
                speak(summary)
            except Exception:
                speak("Sorry, I couldn’t find anything on that topic.")

        elif 'time' in command:
            now = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {now}")

        elif 'open youtube' in command:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")

        elif 'open google' in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")

        elif 'play' in command:
            song = command.replace('play', '').strip()
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

        elif 'stop' in command or 'exit' in command or 'quit' in command:
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("Sorry, I don't understand that. Try again.")

if __name__ == '__main__':
    run_assistant()
