import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser 
import random
import os
import pyautogui
import smtplib

n = random.randint(0,23)
# print(n)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING")

    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON")   

    else:
        speak("GOOD EVENING")  

    speak("I am Jarvis. Let me know how can I help you")       

def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
     
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   ##"C:\Users\somay\Videos\MUSIX\AP-Gurinder-Shinda"

        elif 'play music' in query:
            music_dir = "C:\\Users\\somay\\Videos\\MUSIX\\AP-Gurinder-Shinda"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'screenshot' in query:
              image = pyautogui.screenshot()
              image.save('screenshot.png')
              speak('Screenshot taken.')

        elif 'email to keshav' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "keshav.cse@acem.edu.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. email can't be send")  