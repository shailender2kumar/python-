import speech_recognition as sr
import webbrowser
import pyttsx3
import music
import requests
import openai 
recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="58f04dcc508a4eea9f853bf04717f59e"
def speak(text):
    engine.say(text)
    engine.runAndWait()
def aiProcess(command):
    # openai.api_key="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"
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
           {"role": "system", "content": "You are a helpful assistant."},
         {
            "role": "user",
             "content": command
        }
    ]
    )

    return completion.choices[0].message.content
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.co.in/")
    elif "open x" in c.lower():
        webbrowser.open("https://x.com/")
    elif c.lower().startswith("play"):
         song=c.lower().split(" ")[1]
         link= music.musiic[song]
         print(link)
         webbrowser.open(link)
    elif "news"in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        news_data = r.json()
        
        if news_data['status'] == 'ok':
            articles = news_data.get('articles', [])
            if articles:
                speak("ab tak ki sabse badi.")
                for i, article in enumerate(articles[:5], 1):  # Limit to top 5 news articles
                    speak(f"Headline {i}: {article['title']}")
                    print(f"Headline {i}: {article['title']}")  # Debugging, shows in console
            else:
                speak("Sorry, I couldn't find any news articles.")
    else:
      #useopenai
      output=aiProcess(c)
      speak(output)
if __name__== "__main__" :
    speak("initlazing jarvis ")
while True:
    r=sr.Recognizer()
    
    print("recognizing..")
    try:
       with sr.Microphone() as source:
         print("Listening")      
         audio=r.listen(source,timeout=2,phrase_time_limit=1)
       word=r.recognize_google(audio)
       if(word.lower()=="jarvis"):
         speak("ya")
         with sr.Microphone() as source:
             print("Jarvis Active...")      
             audio=r.listen(source)
             command=r.recognize_google(audio)
         
             
             processcommand(command)
    except Exception as e:
        print("Sphinx error:{0}".format(e))