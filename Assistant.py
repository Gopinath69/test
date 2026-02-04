import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Initialize the speech engine
engine = pyttsx3.init('sapi5') # 'sapi5' is for windows.
voices = engine.getProperty('voices')
# Set voice (0 is usually male/David, 1 is usually female/zira)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    """The function that makes the AI speak."""
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    """Greets the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How may I help you today?")

def take_command():
    """Listenss to miscrophone input ond returns it as a string."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
    return query

def main():
    wish_me()
    while True:
        # Convert query to lower case to make logic matching easier
        query = take_command().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")                           
        elif 'open code' in query:
            #change this path to where your vs code or editor is instaaled.
            codePath = "C:\\Users\\YourUser\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            try:
                os.startfile(codePath)
            except:
                speak("I could not find the path to VS Code.")
        elif 'quit' in query or 'exit' in query or 'stop' in query:
            speak("Good Bye Sir.")
            break

# --- Main Program Execution ---
if __name__ == "__main__":
    main()