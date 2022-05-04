import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Currently Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'john' in command:
                command = command.replace('john', '')

    except:
        pass
    return command


def run_cmd():
    date = datetime.datetime.now().strftime('%A, %B %d, %Y')
    command = take_command()
    print(command)
    if 'play' in command:
        vid = command.replace('play', '')
        talk("playing " + vid)
        print("playing" + vid)
        pywhatkit.playonyt(vid)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('The time is ' + time)
        talk('The time is ' + time)
    elif 'day' in command:
        print('The date is ' + date)
        talk('The date is ' + date)
    elif 'date' in command:
        print('The date is ' + date)
        talk('The date is ' + date)
    elif 'who' in command:
        per1 = command.replace('who', '')
        info1 = wikipedia.summary(per1, 1)
        print(info1)
        talk(info1)
    elif 'what' in command:
        per1 = command.replace('what', '')
        info1 = wikipedia.summary(per1, 1)
        print(info1)
        talk(info1)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'funny' in command:
        talk(pyjokes.get_joke())
    elif 'open chrome' in command:
        chropath = r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chropath)
    else:
        print("I did not understand that, can you repeat it?")
        talk("I did not understand that. Can you repeat that?")


while True:
    run_cmd()
