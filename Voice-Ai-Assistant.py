import pyttsx3
import datetime
from datetime import date
import speechRecognition as sr
import wikipedia
import webbrowser
import smtplib
import os 
import sys
import pywhatkit
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #gets you the details of the current voice
engine.setProperty('voice', voices[1].id)  # 0-male voice , 1-female voice
engine.setProperty("rate", 150)
recognizer=sr.Recognizer() 

def speak(audio):   
  engine.say(audio)    
  engine.runAndWait() #Without this query, speech will not be audible to us.
  
def takeCommand():
    #It takes microphone input from the user and returns string output    
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)
     try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.    
     except Exception as e:
        # print(e)  use only if you want to print the error!
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
     return query
            
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
    
def wishme():
   hour = int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
        speak("Good Morning!")    
    
   elif hour>=12 and hour<18:
        speak("Good Afternoon!")       
    
   else:
        speak("Good Evening!")      
     
if __name__=="__main__" :    
    speak('Hello Sir, I am Bunny, your Artificial intelligence assistant. Please tell me how may I help you')
    wishme()
    while True:
        query = takeCommand().lower() #Converting user query into lower case        
        # Logic for executing tasks based on query
        if 'alexa' in query :
              query = query.replace('alexa', '')
              print('you said'+query)
        else :
 
         print('you said : '+query)
         
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'play music' in query:
            music_dir = 'music_dir_of_the_user'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'open stack overflow' in query :                           
          webbrowser.open('stackoverflow.com')
          
        elif 'open free code camp' in query :            
              webbrowser.open('freecodecamp.org')
              
        elif 'open code' in query:
            codePath = "/Applications/PyCharm CE.app" #that's the code path.
            os.startfile(codePath)
            
        elif "email to receiver's name" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receiver's email id"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")
         
        elif 'hello' in query :
             print('hello how can i helpp you ??')
             speak('hello, how can i help you ??')
         
        elif 'who are you' in query :
             print('I am mini alexa a k a your virtual assistant master')
             speak('I am mini alexa a k a your virtual assistant master. how can i help you ??')
             
        elif 'can you do' in query :
             print('''i can play songs on youtube , tell you a joke, search on wikipedia, tell date and time,find your location, locate area on map,
             open different websites like instagram, youtube,gmail, git hub, stack overflow and searches on google.How may i help you ??''')
             speak('''i can play songs on youtube , tell you a joke, search on wikipedia, tell date and time,find your location, locate area on map,
             open different websites like insta gram, youtube,gmail, git hub, stack overflow and searches on google. How may i help you ??''')
             
        elif 'play' in query:
             song = query.replace('play', '')
             print('Playing' +song)
             speak('Playing' +song)
             pywhatkit.playonyt(song)
        elif 'date and time' in query :
             today = date.today()
             time = datetime.datetime.now().strftime('%I:%M %p')
             # Textual month, day and year 
             d2 = today.strftime("%B %d, %Y")
             print("Today's Date is ", d2, 'Current time is', time)
             speak('Today is : '+ d2)
             speak('and current time is '+ time)
         
        elif 'time and date' in query :
             today = date.today()
             time = datetime.datetime.now().strftime('%I:%M %p')
             # Textual month, day and year 
             d2 = today.strftime("%B %d, %Y")
             print("Today's Date is ", d2, 'Current time is', time)
             speak( 'Current time is '+ time)
             speak('and Today is : '+ d2)
             
             
        elif 'time' in query:
             time = datetime.datetime.now().strftime('%I:%M %p')
             print('The current time is' +time)
             speak('The current time is')
             speak(time)
             
        elif 'date' in query:
             today = date.today()
             print("Today's date:", today)
             # Textual month, day and year 
             d2 = today.strftime("%B %d, %Y")
             print("Today's Date is ", d2)
             speak('The todays date is')
             speak(d2)
         
        elif 'tell me about' in query:
             name = query.replace('tell me about' , '')
             info = wikipedia.summary(name, 1)
             print(info)
             speak(info)
             
        elif 'wikipedia' in query:
             name = query.replace('wikipedia' , '')
             info = wikipedia.summary(name, 1)
             print(info)
             speak(info)
        elif 'what is' in query:
             name = query.replace('what is ' , '')
             info = wikipedia.summary(name, 1)
             print(info)
             speak(info)
         
        elif 'who is ' in query:
             name = query.replace('who is' , '')
             info = wikipedia.summary(name, 1)
             print(info)
             speak(info)
             
        elif 'what is ' in query :
             search = 'https://www.google.com/search?q='+query
             print(' Here is what i found on the internet..')
             speak('searching... Here is what i found on the internet..')
             webbrowser.open(search)
             
        elif 'joke' in query:
             _joke = pyjokes.get_joke()
             print(_joke)
             speak(_joke)
             
        elif 'search' in query :
             search = 'https://www.google.com/search?q='+query
             speak('searching... ')
             webbrowser.open(search)
         
        elif "my location" in query:
             url = "https://www.google.com/maps/search/Where+am+I+?/"
             webbrowser.get().open(url)
             speak("You must be somewhere near here, as per Google maps") 
        elif 'locate ' in query :
             speak('locating ...')
             loc = query.replace('locate', '')
             if 'on map' in loc :
                 loc= loc.replace('on map',' ')
                 url = 'https://google.nl/maps/place/'+loc+'/&amp;'
                 webbrowser.get().open(url)
                 print('Here is the location of '+loc)
                 speak('Here is the location of '+loc)
         
        elif 'on map' in query :
             speak('locating ...')
             loc = query.split(" ")
             print(loc[1])
             url = 'https://google.nl/maps/place/'+loc[1] +'/&amp;'
             webbrowser.get().open(url)
             print('Here is the location of '+loc[1])
             speak('Here is the location of '+loc[1])
         
         
        elif 'location of' in query :
             speak('locating ...')
             loc = query.replace('find location of', '')
             url = 'https://google.nl/maps/place/'+loc+'/&amp;'
             webbrowser.get().open(url)
             print('Here is the location of '+loc)
             speak('Here is the location of '+loc)
         
         
        elif 'where is ' in query :
             speak('locating ...')
             loc = query.replace('where is', '')
             url = 'https://google.nl/maps/place/'+loc+'/&amp;'
             webbrowser.get().open(url)
             print('Here is the location of '+loc)
             speak('Here is the location of '+loc)
             
        elif 'bootcamps' in query :
             search = 'http://tathastu.twowaits.in/index.html#courses'
             speak('opening boot camps')
             webbrowser.open(search)
             
        elif 'boot camps' in query :
             search = 'http://tathastu.twowaits.in/index.html#courses'
             speak('opening boot camps')
             webbrowser.open(search)
         
        elif 'python bootcamp' in query :
             search = 'http://tathastu.twowaits.in/kickstart_python.html'
             speak('showing pythonboot camp')
             webbrowser.open(search)
             
        elif 'data science bootcamp' in query :
             search = 'http://tathastu.twowaits.in/kickstart_data_science.html'
             speak('showing data science and ml bootcamp')
             webbrowser.open(search)
         
        elif 'open google' in query :
             print('opening google ...')
             speak('opening google..')
             webbrowser.open_new('https://www.google.co.in/')
         
        elif 'gmail' in query :
             print('opening gmail ...')
             speak('opening gmail..')
             webbrowser.open_new('https://mail.google.com/')
             
        elif 'open youtube' in query :
             print('opening you tube ...')
             speak('opening you tube..')
             webbrowser.open_new('https://www.youtube.com/')
        elif 'open instagram' in query :
             print('opening instagram ...')
             speak('opening insta gram...')
             webbrowser.open_new('https://www.instagram.com/')
         
        elif 'open stack overflow' in query :
             print('opening stackoverflow ...')
             speak('opening stack overflow...')
             webbrowser.open_new('https://stackoverflow.com/')
             
        elif 'open github' in query :
             print('opening git hub ...')
             speak('opening git hub...')
             webbrowser.open_new('https://github.com/')
         
        elif 'bye' in query:
             print('good bye, have a nice day !!')
             speak('good bye, have a nice day !!')
             sys.exit()
         
        elif 'thank you' in query :
             print("your welcome")
             speak('your welcome')
         
        elif 'stop' in query:
             print('good bye, have a nice day !!')
             speak('good bye, have a nice day !!')
             sys.exit()
         
        elif 'tata' in query:
             print('good bye, have a nice day !!')
             speak('good bye, have a nice day !!')
             sys.exit()
             
        else:
             print(' Here is what i found on the internet..')
             speak('Here is what i found on the internet..')
             search = 'https://www.google.com/search?q='+query
             webbrowser.open(search)