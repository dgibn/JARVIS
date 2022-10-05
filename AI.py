import webbrowser
"""opening the browser"""
import pyttsx3 
"""initialising the type of voice"""
import os
from bs4 import BeautifulSoup
from setup import get_calendar_service
import pycountry
import random
import datetime
import wikipedia
import json
import requests
import subprocess
import speech_recognition as src
from ecapture import ecapture as ec
import wolframalpha
import time
engine=pyttsx3.init("sapi5")
rate=engine.getProperty("rate")
engine.setProperty("rate", rate-5)
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wish():
    now=datetime.datetime.now().hour
    if now<12:
        speak("Good Morning Divyam")
        print("Good Morning")
    elif now>=12 and now<=16:
        speak("Good Afternoon Divyam")
        print("Good Afternoon")
    else:
        speak("Good Evening Divyam")
        print("Good Evening")
print("Loading your AI")
speak("Hello")
speak(" I am your personal AI ")
speak("Jarvis")
wish()
def takecommand():
    r=src.Recognizer()
    with src.Microphone() as source:
        print("Listening.....")
        audio=r.listen(source,phrase_time_limit=5)
        try:
            statement=r.recognize_google(audio,language="en-in")
            print(f"User said {statement}\n")
        except Exception as e:
            speak("Perdone")
            return "None"
        return statement
speak("How u doin")
statement=takecommand().lower()
if "what about you" in statement:
    speak("I am doing great")
    speak("What can i do for you")
    if __name__ == '__main__':
        while True:
            statement=takecommand().lower()
            if statement==0:
                continue
            if "goodbye veronica" in statement or "ok bye" in statement or "no" in statement: 
                speak("Shutting down")
            if "upcoming events" in statement:
                def main():
                    service=get_calendar_service()
                    now=datetime.datetime.utcnow().isoformat() + "Z"
                    print("Getting the list")
                    events_results=service.events().list(calendarId="primary",timeMin=now,maxResults=10,singleEvents=True,orderBy="startTime").execute()
                    events=events_results.get("items",[])
                    if not events:
                        speak("No upcoming events")
                    for event in events:
                        t=event["start"]["dateTime"][0:10],event['summary']
                        speak(t)
                if __name__=="__main__":
                    main()
                time.sleep(4)
                speak("Anything else")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
            if "wikipedia" in statement:
                speak("What do you want to search for")
                statement=takecommand().lower()
                results=wikipedia.summary(statement,sentences=3)
                speak("according to wikipedia")
                speak(results)
                print(results)
                time.sleep(4)
                speak("Anything else")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
            if "open" in statement:
                r=str(statement)
                webbrowser.open_new_tab("https://{}.com".format(r[5:]))
                speak("opening {}".format(r[5:]))
                time.sleep(5)
                speak("Anything else")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
            if "timer" in statement:
                r=str(f"{statement}")
                t=r.split()
                m=0
                s=0
                h=0
                p=0
                if "minutes" in t:
                    m=m+int(t[t.index("minutes")-1])
                if "seconds" in t:
                    s+=int(t[t.index("seconds")-1])
                if "hours" in t:
                    h+=int(t[t.index("hours")-1])
                if h==0:
                    if m==0:
                        st=("Setting a timer for {} seconds").format(s)
                    else:
                        st=("Setting a timer for {} minutes {} seconds").format(m,s)
                elif h==1:
                    if m==0:
                        st=("Setting a timer for 1 hour {} seconds").format(s)
                    else:
                        st=("Setting a timer for 1 hours {} minutes {} seconds").format(m,s)
                else:
                    if m==0:
                        st=("Setting a timer for {} hours {} seconds").format(h,s)
                    else:
                        st=("Setting a timer for {} hours {} minutes {} seconds").format(h,m,s)
                speak(st)
                a=(h*3600)+(m*60)+s
                while p<a:
                    time.sleep(1)
                    p=p+1
                speak("Time Up!")
                time.sleep(5)
                speak("Anything else")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
                
                
            if "what is the time" in statement or "what is the time veronica" in statement:
                t=datetime.datetime.now().strftime("%H:%M:%S")
                speak("Right now the time is {}".format(t))
                time.sleep(4)
                speak("Anything else")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
            if "what is the date today" in statement:
                t=datetime.date.today()
                speak("Today is {}".format(t))
                time.sleep(4)
                speak("Anything else")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
            if "generate password" in statement:
                a="abcdefghijklmnopqrstuvwxyz"
                b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                c="0123456789"
                d="*&%^$!@#~:;"
                length=random.randrange(9,15)
                all=a+b+c+d
                password="".join(random.sample(all, length))
                print(password)
                speak(password)
                time.sleep(4)
                speak("Anything else")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
            if "who are you" in statement:
                speak("I am Jarvis. Personal AI made by Divyam. I am in my beta version.")
                time.sleep(4)
                speak("Anything else")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
         
            if "search for" in statement:
                statement=statement.replace("search for","")
                webbrowser.open_new_tab(statement)
                time.sleep(10)
                speak("Anything else")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
            if "news" in statement:
                url="https://timesofindia.indiatimes.com/"
                res=requests.get(url)
                if res.status_code==200:
                    print("Successfully opened")
                    soup=BeautifulSoup(res.text,"html.parser")
                    l=soup.find("div",{"class":"_1CfcV"})
                    for i in l.findAll("a"):
                        speak(i.text)
                else:
                    print("Error")
                time.sleep(4)
                speak("Anything else")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
            if "nothing" in statement:
                speak("You sure?")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
            if "logoff" in statement or "log off" in statement or "shut down my laptop" in statement:
                speak("Shutting down your laptop")
                subprocess.call(["shutdown","/l"])
else:
    speak("Okay what can i do for you today")
    if __name__ == '__main__':
        while True:
            statement=takecommand().lower()
            if statement==0:
                continue
            if "goodbye veronica" in statement or "ok bye" in statement or "no" in statement: 
                speak("Shutting down")
            if "upcoming events" in statement:
                def main():
                    service=get_calendar_service()
                    now=datetime.datetime.utcnow().isoformat() + "Z"
                    print("Getting the list")
                    events_results=service.events().list(calendarId="primary",timeMin=now,maxResults=10,singleEvents=True,orderBy="startTime").execute()
                    events=events_results.get("items",[])
                    if not events:
                        speak("No upcoming events")
                    for event in events:
                        t=event["start"]["dateTime"][0:10],event['summary']
                        speak(t)
                if __name__=="__main__":
                    main()
                time.sleep(4)
                speak("Anything else")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
            if "wikipedia" in statement:
                speak("What do you want to search for")
                statement=takecommand().lower()
                results=wikipedia.summary(statement,sentences=3)
                speak("according to wikipedia")
                speak(results)
                print(results)
                time.sleep(4)
                speak("Anything else")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
            if "open" in statement:
                r=str(statement)
                webbrowser.open_new_tab("https://{}.com".format(r[5:]))
                speak("opening {}".format(r[5:]))
                time.sleep(5)
                speak("Anything else")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
            if "timer" in statement:
                r=str(f"{statement}")
                t=r.split()
                m=0
                s=0
                h=0
                p=0
                if "minutes" in t:
                    m=m+int(t[t.index("minutes")-1])
                if "seconds" in t:
                    s+=int(t[t.index("seconds")-1])
                if "hours" in t:
                    h+=int(t[t.index("hours")-1])
                if h==0:
                    if m==0:
                        st=("Setting a timer for {} seconds").format(s)
                    else:
                        st=("Setting a timer for {} minutes {} seconds").format(m,s)
                elif h==1:
                    if m==0:
                        st=("Setting a timer for 1 hour {} seconds").format(s)
                    else:
                        st=("Setting a timer for 1 hours {} minutes {} seconds").format(m,s)
                else:
                    if m==0:
                        st=("Setting a timer for {} hours {} seconds").format(h,s)
                    else:
                        st=("Setting a timer for {} hours {} minutes {} seconds").format(h,m,s)
                speak(st)
                a=(h*3600)+(m*60)+s
                while p<a:
                    time.sleep(1)
                    p=p+1
                speak("Time Up!")
                time.sleep(5)
                speak("Anything else")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
                
            if "what is the time" in statement or "what is the time veronica" in statement:
                t=datetime.datetime.now().strftime("%H:%M:%S")
                speak("Right now the time is {}".format(t))
                time.sleep(4)
                speak("Anything else")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
            if "what is the date today" in statement:
                t=datetime.date.today()
                speak("Today is {}".format(t))
                time.sleep(4)
                speak("Anything else")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
            if "generate password" in statement:
                a="abcdefghijklmnopqrstuvwxyz"
                b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                c="0123456789"
                d="*&%^$!@#~:;"
                length=random.randrange(9,15)
                all=a+b+c+d
                password="".join(random.sample(all, length))
                print(password)
                speak(password)
                time.sleep(4)
                speak("Anything else")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
            if "who are you" in statement:
                speak("I am Jarvis. Personal AI made by Divyam. I am in my beta version.")
                time.sleep(4)
                speak("Anything else")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
         
            if "search for" in statement:
                statement=statement.replace("search for","")
                webbrowser.open_new_tab(statement)
                time.sleep(10)
                speak("Anything else")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
            if "news" in statement:
                url="https://timesofindia.indiatimes.com/"
                res=requests.get(url)
                if res.status_code==200:
                    print("Successfully opened")
                    soup=BeautifulSoup(res.text,"html.parser")
                    l=soup.find("div",{"class":"_1CfcV"})
                    for i in l.findAll("a"):
                        speak(i.text)
                else:
                    print("Error")
                time.sleep(4)
                speak("Anything else")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
            if "nothing" in statement:
                speak("You sure?")
                statement=takecommand().lower()
                if "no" in statement or statement==0:
                    break
            if "logoff" in statement or "log off" in statement or "shut down my laptop" in statement:
                speak("Shutting down your laptop")
                subprocess.call(["shutdown","/l"])
            else:
                break