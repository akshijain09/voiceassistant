import datetime
import nltk
import speech_recognition as sr
import pyttsx3
import requests
from bs4 import BeautifulSoup

url="https://akshijain09.github.io/demo/"

headers={
   'Accept-Encoding': 'gzip, deflate, br',
   'Accept-Language': 'en-US,en;q=0.9',
   'User-Agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Connection': 'keep-alive'

}
r=requests.get(url=url,headers=headers)
soup=BeautifulSoup(r.text,'html.parser')


listener = sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[5].id)
engine.setProperty("rate",170)


def speak(listener):
    engine.say(listener)
    print(listener)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=8 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("Hi  I am Bhanumati. What can I do for you.")

def takecommand():

    listener = sr.Recognizer()
    with sr.Microphone() as source:
        #listener.adjust_for_ambient_noise(source, duration=1)
        print('listening..')
        listener.pause_threshold = 1
        voice = listener.listen(source,None,3)
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        if ' indian toys' in command:
            # print(command)
            engine.say('which state you want to know about')
            engine.runAndWait()
            takestate()
        elif 'introduction' in command:
            speak("Hi I am your bhanumati. I am here to spread "
                  "awareness about Indian toys. I  can tell about indian folk tales , cultural and mythological stories. I support VOCAL FOR LOCAL"
                  " and sustainability.")
            stop()

        elif 'mythological' in command:
            speak("Which mythological story you want to listen")
            takemythology()
        elif 'cultural'in command:
            speak("Which cultural story you want to listen")
            takecultural()
        elif 'folk tails'in command:
            speak("Which folk tail you want to listen")
            takefolktail()

        elif 'stop' in command:
            speak('hope to meet you soon,have a nice day')



        else:
           speak("this content is not available")
           stop()

    except Exception as e:
        speak("Say that again please")
        takecommand()
def stop():
    speak("Do you want Anything Else")
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        # listener.adjust_for_ambient_noise(source, duration=1)
        print('listening..')
        listener.pause_threshold = 1
        voice = listener.listen(source, None, 3)
    try:
        command = listener.recognize_google(voice)
        command = command.lower()

        if 'stop'in command:
            speak("hope to meet you soon,have a nice day!")
        else:
            takecommand()

    except Exception as e:
        speak('speak that again please')










def takestate():
        with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source, duration=1)
                print('listening..')
                voices = listener.listen(source)
        try:
                commands = listener.recognize_google(voices)
                commands = commands.lower()

                if 'jammu and kashmir' in commands:
                        div_bs4 = soup.find('div', id="jammu")
                        print(commands)
                        print(div_bs4)
                        engine.say(div_bs4)
                        engine.runAndWait()
                        stop()
                elif 'himachal pradesh' in commands:
                        div_bs4 = soup.find('div', id="himachal")
                        print(div_bs4)
                        engine.say(div_bs4)
                        engine.runAndWait()
                        stop()
                elif 'uttarakhand' in commands:
                       div_bs4 = soup.find('div', id="uttrakhand")
                       print(div_bs4)
                       engine.say(div_bs4)
                       engine.runAndWait()
                       stop()
                elif 'punjab' in commands:
                       div_bs4 = soup.find('div', id="punjab")
                       print(div_bs4)
                       engine.say(div_bs4)
                       engine.runAndWait()
                       stop()
                elif 'haryana'in commands:
                       div_bs4 = soup.find('div', id="haryana")
                       print(div_bs4)
                       engine.say(div_bs4)
                       engine.runAndWait()
                       stop()
                elif 'chandigarh' in commands:
                       div_bs4 = soup.find('div', id="chandigarh")
                       print(div_bs4)
                       engine.say(div_bs4)
                       engine.runAndWait()
                       stop()
                elif 'delhi' in commands:
                       div_bs4 = soup.find('div', id="delhi")
                       print(div_bs4)
                       engine.say(div_bs4)
                       engine.runAndWait()
                       stop()
                elif 'rajasthan'in commands:
                       div_bs4 = soup.find('div', id="rajasthan")
                       print(div_bs4)
                       engine.say(div_bs4)
                       engine.runAndWait()
                       stop()
                elif 'uttarpradesh'in commands:
                       div_bs4 = soup.find('div', id="uttarpradesh")
                       print(div_bs4)
                       engine.say(div_bs4)
                       engine.runAndWait()
                       stop()
                elif 'gujarat'in commands:
                       div_bs4 = soup.find('div', id="gujrat")
                       print(div_bs4)
                       engine.say(div_bs4)
                       engine.runAndWait()
                       stop()
                elif 'daman and diu'in commands:
                       div_bs4 = soup.find('div', id="daman")
                       print(div_bs4)
                       engine.say(div_bs4)
                       engine.runAndWait()
                       stop()
                elif 'maharashtra' in commands:
                       div_bs4 = soup.find('div', id="maharashtra")
                       print(div_bs4)
                       engine.say(div_bs4)
                       engine.runAndWait()
                       stop()
                elif 'goa' in commands:
                       div_bs4 = soup.find('div', id="goa")
                       print(div_bs4)
                       engine.say(div_bs4)
                       engine.runAndWait()
                       stop()
                elif 'madhyapradesh' in commands:
                      div_bs4 = soup.find('div', id="mp")
                      print(div_bs4)
                      engine.say(div_bs4)
                      engine.runAndWait()
                      stop()
                elif 'chhattisgarh' in commands:
                      div_bs4 = soup.find('div', id="chattisgarh")
                      print(div_bs4)
                      engine.say(div_bs4)
                      engine.runAndWait()
                      stop()



                elif 'andhrapradesh' in commands:
                      div_bs4 = soup.find('div', id="ap")
                      print(div_bs4)
                      engine.say(div_bs4)
                      engine.runAndWait()
                      stop()
                elif 'telangana'in commands:
                      div_bs4 = soup.find('div', id="telangana")
                      print(div_bs4)
                      engine.say(div_bs4)
                      engine.runAndWait()
                      stop()
                elif 'karnataka' in commands:
                      div_bs4 = soup.find('div', id="karnataka")
                      print(div_bs4)
                      engine.say(div_bs4)
                      engine.runAndWait()
                      stop()
                elif 'kerala' in commands:
                      div_bs4 = soup.find('div', id="kerla")
                      print(div_bs4)
                      engine.say(div_bs4)
                      engine.runAndWait()
                      stop()
                elif 'tamilnadu'in commands:
                      div_bs4 = soup.find('div', id="tamil")
                      print(div_bs4)
                      engine.say(div_bs4)
                      engine.runAndWait()
                      stop()
                elif'bihar'in commands:
                      div_bs4 = soup.find('div', id="bihar")
                      print(div_bs4)
                      engine.say(div_bs4)
                      engine.runAndWait()
                      stop()
                elif'jharkhand'in commands:
                      div_bs4 = soup.find('div', id="jharkhand")
                      print(div_bs4)
                      engine.say(div_bs4)
                      engine.runAndWait()
                      stop()
                elif 'odisha'in commands:
                       div_bs4=soup.find('div',id="odisha")
                       print(div_bs4)
                       engine.say(div_bs4)
                       engine.runAndWait()
                       stop()
                elif 'westbengal'in commands:
                      div_bs4=soup.find('div',id="bengal")
                      print(div_bs4)
                      engine.say(div_bs4)
                      engine.runAndWait()
                      stop()
                elif'andaman and nicobar' in commands:
                      div_bs4=soup.find('div',id="andman")
                      print(div_bs4)
                      engine.say(div_bs4)
                      engine.runAndWait()
                      stop()
                else:
                       speak("This content is not available")
                       stop()

        except Exception as e:
                speak("Say that state again please")
                takestate()

def takemythology():
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source,duration=1)
        print('listening')
        voices=listener.listen(source)
    try:
        commandm=listener.recognize_google(voices)
        commandm=commandm.lower()

        if'ekalavya' in commandm:
            div_bs4=soup.find('div',id="eklavya")
            print(commandm)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        elif 'surdas'in commandm:
            div_bs4 = soup.find('div', id="surdas")
            print(commandm)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        elif'abhimanyu' in commandm:
            div_bs4 = soup.find('div', id="abhimanyu")
            print(commandm)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        elif 'prahlada' in commandm:
            div_bs4 = soup.find('div', id="prahalda")
            print(commandm)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        elif 'shravan 'in commandm:
            div_bs4 = soup.find('div', id="shravan")
            print(commandm)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        elif 'ganesha'in commandm:
            div_bs4 = soup.find('div', id="ganesha")
            print(commandm)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        elif 'krishna' in commandm:
            div_bs4 = soup.find('div', id="krishna")
            print(commandm)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        elif 'vibhishana'in commandm:
            div_bs4 = soup.find('div', id="vibishana")
            print(commandm)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        else:
            speak("This content is not available")
            stop()
    except Exception as e:
        speak("Say the name of that mythological story again ")
        takemythology()

def takecultural():
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source,duration=1)
        print('listening')
        voices=listener.listen(source)
    try:
        commands=listener.recognize_google(voices)
        commands=commands.lower()
        if 'diwali' in commands:
            div_bs4 = soup.find('div', id="diwali")
            print(commands)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        elif 'janmashtami'in commands:
            div_bs4 = soup.find('div', id="janmasthmi")
            print(commands)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        elif 'mahashivratri'in commands:
            div_bs4 = soup.find('div', id="mahashivratri")
            print(commands)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        elif 'holi'in commands:
            div_bs4 = soup.find('div', id="holi")
            print(commands)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        elif 'ganesh chaturthi'in commands:
            div_bs4 = soup.find('div', id="ganeshchaturthi")
            print(commands)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        elif 'makarsakranti'in commands:
            div_bs4 = soup.find('div', id="makarsakranti")
            print(commands)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        else:
           speak("This content is not available")
           stop()
    except Exception as e:
        speak("Say the name of that cultural story again ")
        takecultural()


def takefolktail():
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source,duration=1)
        print('listening')
        voices=listener.listen(source)
    try:
        commands=listener.recognize_google(voices)
        commands=commands.lower()
        if 'baital pachisi' in commands:
            div_bs4 = soup.find('div', id="baital")
            print(commands)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        elif 'The wedding of the mouse' in commands:
            div_bs4 = soup.find('div', id="mouse")
            print(commands)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        elif ('sulasa') or ('jataka') in commands:
            div_bs4 = soup.find('div', id="sulasajataka")
            print(commands)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        elif 'wives' in commands:
            div_bs4 = soup.find('div', id="wives")
            print(commands)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        elif 'mongoose' in commands:
            div_bs4 = soup.find('div', id="mangoose")
            print(commands)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        elif ('akbar') or ('birbal') in commands:
            div_bs4 = soup.find('div', id="mangoose")
            print(commands)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        elif 'tenali' in commands:
            div_bs4 = soup.find('div', id="mangoose")
            print(commands)
            print(div_bs4)
            engine.say(div_bs4)
            engine.runAndWait()
            stop()
        else:
            speak("This content is not available")
            stop()
    except Exception as e:
        speak("Say the name of that cultural story again ")
        takecultural()













































    except Exception as e:
        speak("Say the name of story again please")








if __name__ == "__main__":
    wish()
    takecommand()


