import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
from difflib import get_close_matches
import wikipedia
import keyboard
from time import sleep
from PyDictionary import PyDictionary
import pywhatkit
from speak import speak
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
rate=engine.getProperty('rate')
engine.setProperty("rate",rate-30)
chose=0
# def speak(text):
#     print("Jarvis:",text)
#     engine.say(text)
#     engine.runAndWait()

def listen_to_user():
    count=0
    r = sr.Recognizer()
    while count<3:
        with sr.Microphone() as source:
            audio = r.listen(source,5,5)
        try:
            query = r.recognize_google(audio, language='en-in')
            return query
            count=4


        except sr.UnknownValueError:
            count+=1

def command(query):
    global chose
    patterns=['activate automatic skip ad mode', 'launch rock paper scissor game','activate akinator mode','hello','open','time','what time is going on','youtube','dictionary','play music','search google','question','next','what is your name','stop']
    q=get_close_matches(query.lower(),patterns)
    print(q)
    print(query)
    if q==[]:
        if query[:4].lower()=='open':
            speak("opening")
            str1=[query[4:]]
            keyboard.press_and_release("windows")
            sleep(3)
            keyboard.write(str1[0])
            sleep(4)
            keyboard.press("enter")
        elif query[:5].lower()=="close":
            import closeapp
            st=[query[5:]]
            closeapp.close(st[0])
            speak("closed")
            
        else:
            speak("This command not available")
            speak("try again sir")
    else:
        if q[0]=="time" or q[0]=='what time is going on':
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Time is {strtime}")

        elif  q[0]=='dictionary':
            m=PyDictionary()
            speak("enter word sir")
            w=listen_to_user()
            try:
                speak(m.translate(w,'en'))
                speak(m.meaning(w))
            except:
                speak("try again")

        elif q[0]=='youtube':
                speak("search for:")
                search=listen_to_user()
                if search==None:
                    webbrowser.open("https://www.youtube.com/")
                    speak("i'm not able to get your search command")
                    speak("i'm opening youtube homepage")
                    speak("opening youtube")
                else:
                    pywhatkit.playonyt(search)
                    speak('opening')

        elif q[0]=='play music':
            import os
            m='e:\\songs'
            song=os.listdir(m)
            length=len(song)
            speak("now music is playing")
            os.startfile(os.path.join(m,song[chose]))
            chose+=1
        elif q[0]=='next':
            import os
            m='e:\\songs'
            song=os.listdir(m)
            length=len(song)
            if chose>=length:
                speak("no more music to next")
                speak("i'm playing music from starting")
                chose=0
                os.startfile(os.path.join(m,song[chose]))
            else:
                os.startfile(os.path.join(m,song[chose]))
                chose+=1
        elif q[0]=='stop':
            from os import system
            speak('ok boss')
            speak("now i stop music")
            system('taskkill /F /FI "WINDOWTITLE eq Movies & Tv" ')
            system('taskkill /F /FI "WINDOWTITLE eq Groove Music" ')
        elif q[0]=='search google':
            speak("what for searching")
            g=listen_to_user()
            if g is not None:
                webbrowser.open("https://www.google.com/search?q=" + g)
                speak("google chrome now poping")
            else:
                speak("i'm not able to get search query")
                speak("opening google home page")
                webbrowser.open("https://www.google.com/")

        elif q[0]=='question':
            speak("what's your question sir")
            question=listen_to_user()
            ans=wikipedia.summary(question,sentences=2)
            speak("According to wikipedia")
            speak(ans)
            speak("do you want to more:")
            more=listen_to_user()
            if more=='y' or more=='yes':
                answer=wikipedia.summary(question)
                speak(answer)

            else:
                None

        elif q[0]=='close google chrome':
            from os import system
            speak("now i stop google chrome")
            system("taskkill /f /im chrome.exe")
        elif q[0]=='open':
            speak("opening")
            str1=[query[4:]]
            keyboard.press_and_release("windows+s")
            sleep(1)
            keyboard.write(str1[0])
            sleep(1)
            keyboard.press("enter")

        elif q[0]=='open google chrome':
            speak("opening")
            keyboard.press_and_release("windows+s")
            sleep(1)
            keyboard.write('google chrome')
            sleep(1)
            keyboard.press("enter")
        elif q[0]=="hello":
            speak("hii sir")
        elif q[0]=="activate akinator mode":
            import os
            speak("activating")
            os.startfile("ak.py")
        elif q[0]=="launch rock paper scissor game":
            import os
            speak("launching")
            os.startfile("game.py")
        elif q[0]=="activate automatic skip ad mode":
            import os 
            speak("activating")
            os.system("taskkill /im chrome.exe")
            os.startfile("autoskipad.py")
            speak("activated")


def getcommand():
    file=open("myfile.txt",'r')
    line=file.readlines()
    query=line[0]
    command(query)


getcommand()
