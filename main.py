import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
listener = sr.Recognizer()
google = pyttsx3.init()
voices = google.getProperty('voices')
google.setProperty('voice',voices[1].id)
def talk (text):
        google.say(text)
        google.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source :
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'google' in command :
                 command = command.replace('google', '')
    except:
           pass
    return command
def run_google():
       command = take_command()
       if 'time' in command:
               time = datetime.datetime.now().strftime('%I:%M')
               print(time)
               talk('current time is'+ time)

       elif 'play' in command:
           song = command.replace('play', '')
           talk('playing' + song)
           pywhatkit.playonyt(song)
       elif 'tell me about' in command :
           lookfor = command.replace('tell me about', '')
           info = wikipedia.summary(lookfor, 1)
           print(info)
           talk(info)
       elif 'joke' in command :
           talk(pyjokes.get_joke())
       else:
           talk('i dont understand i search google')
           pywhatkit.search(command)


while True:
        run_google()