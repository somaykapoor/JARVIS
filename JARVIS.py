import pyttsx3                      ##ALL THE LIRARIES
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser 
import random
import os
import pyautogui
import smtplib
import sys

from PyQt5 import QtWidgets, QtCore, QtGui    ##GUI LIBRARIES
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JarvisGUI_2 import Ui_MainWindow
from sys import argv,exit

n = random.randint(0,23)
# print(n)

engine = pyttsx3.init('sapi5')           ##VOICE OUTPUT FNS
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):                        ##VOICE INPUT FNS
    engine.say(audio)                      
    engine.runAndWait()


def wishMe():                            ##WISHME FNS

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING")

    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON")   

    else:
        speak("GOOD EVENING")  

    speak("I am Jarvis. Let me know how can I help you") 


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()
            

    def takeCommand(self):                   ##TAKE COMMAND FNS
        

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.5
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            self.query = r.recognize_google(audio, language='en-in')
            print(f"User said: {self.query}\n")

        except Exception as e:
        
            print("Say that again please...")  
            return "None"
        self.query = self.query.lower()    
        return self.query


    def TaskExecution(self):                ##TASK EXECUTION FNS
            wishMe()
            while True: 
    
                self.query = self.takeCommand()

                if 'wikipedia' in self.query:
                    speak('Searching Wikipedia...')
                    self.query = self.query.replace("wikipedia", "")
                    results = wikipedia.summary(self.query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'open youtube' in self.query:
                    webbrowser.open("youtube.com")

                elif 'open google' in self.query:
                    webbrowser.open("google.com")

                elif 'open stackoverflow' in self.query:
                    webbrowser.open("stackoverflow.com")   ##"C:\Users\somay\Videos\MUSIX\AP-Gurinder-Shinda"

                elif 'play music' in self.query:
                    music_dir ="C:\Users\somay\Videos\MUSIX"
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[n]))

                elif 'the time' in self.query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")

                elif 'open code' in self.query:
                    codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)

                elif 'screenshot' in self.query:
                    image = pyautogui.screenshot()
                    image.save('screenshot.png')
                    speak('Screenshot taken.')

                elif 'email to keshav' in self.query:
                    try:
                        speak("What should I say?")
                        content = self.takeCommand()
                        to = "keshav.cse@acem.edu.in"    
                        sendEmail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("Sorry. email can't be send")  

startExecution = MainThread()

class Main(QMainWindow):               ##OOPS BASED CMD FOR GUI
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Startbutton.clicked.connect(self.StartTask)
        self.ui.Quit_button.clicked.connect(self.close)
        self.ui.YT_pushbutton.clicked.connect(self.youtube)
        self.ui.Chrome_pushbutton.clicked.connect(self.chrome)

    def youtube(self):
        webbrowser.open("youtube.com")  

    def chrome(self):
        webbrowser.open("google.com")  
        

    def StartTask(self):
        self.ui.movie = QtGui.QMovie("initial.gif")
        self.ui.Gif_1.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("jarvis-iron-man.gif")
        self.ui.Gif_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("d6a4db7983112c867f7ec4d71e754292.gif")
        self.ui.Gif_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

app = QApplication(sys.argv)
Jarvis = Main()
Jarvis.show()
exit(app.exec_())

