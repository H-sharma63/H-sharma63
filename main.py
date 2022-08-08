import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


# text to speach
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception:
            speak("say that again please...")
            return "none"
        return query


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour >= 12 and hour <= 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am jarvis sir. please tell me how can I help you")


# to send email
def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("your id and password")
    server.sendmail('your id', to, content)
    server.close()


if __name__ == "__main__":
    wish()
    while True:
        if 1:

            query = takecommand().lower()

            # logic building for task

            if "open notepad" in query:
                npath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)

            elif "open adobe reader" in query:
                apath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader.exe"
                os.startfile(apath)

            elif "open command prompt" in query:
                os.startfile("start cmd")

            elif "open camera" in query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break;
                cap.release()
                cv2.destroyAllWindows()

            elif "play music" in query:
                misic_dir = "C:\\Users\\Default\\Music"
                songs = os.listdir(misic_dir)
                rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(misic_dir, song))



            elif "ip address" in query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "wikipedia" in query:
                speak("searching wikipedia....")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("according wikipedia")
                speak(results)
            # print(results)

            elif "open youtube" in query:
                webbrowser.open("https://www.youtube.com/")

            elif "open google" in query:
                speak("sir what should i search on google")
                cm = takecommand().lower()
                webbrowser.open(f"{cm}")

            elif "open instagram" in query:
                webbrowser.open("https://www.instagram.com/")

            elif "open facebook" in query:
                webbrowser.open("https://www.facebook.com/")

            elif "open gmail" in query:
                webbrowser.open("https://www.gmail.com/")

            elif "open Whatsapp" in query:
                webbrowser.open("https://web.whatsapp.com/")

            elif "play song on youtube" in query:
                kit.playonyt("so high")

            elif "emil to person" in query:
                try:
                    speak("what should i say?")
                    content = takecommand().lower()
                    to = "recever id"
                    sendemail(to, content)
                    speak("Email has been sent to Harshit")

                except Exception as e:
                    print(e)
                    print("sorry sir, I am not able to sent this mail to Harshit")

            elif "no thanks" in query:
                speak("thanks for using me have a good day.")
                sys.exit()

            speak("sir do you have any other work")

# to set an alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
                music_dir = 'C:\\Users\\Default\\Music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))
# to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
