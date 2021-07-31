import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("good afternoon")

    else:
        speak("Good Evening")

    speak("I am jarvis sir,please tell me how can i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query


if __name__ == "__main__":
    speak("Anurag is a good boy")
    wishMe()
    query = takeCommand().lower()

    while (True):
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            break

        elif 'open google' in query:
            webbrowser.open("www.google.com")
            break

        elif 'open stack overflow' in query:
            webbrowser.open("www.stackoverflow.com")
            break

        elif 'the time ' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
            break

        elif 'open sublime text' in query:
            codepath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(codepath)
            break

        else:
            speak("Sir,Please say some valid command!")
            break





























