import smtplib
import speech_recognition as sr
import pyttsx3
from  email.message import EmailMessage
def speak(text):
    engine.say(text)
    engine.runAndWait()
i=0
engine=pyttsx3.init()
def mic() :
    r=sr.Recognizer()
    with sr.Microphone() as source:
      print("recognizing..")
      print("Listening")  
      r.adjust_for_ambient_noise(source)    
      audio=r.listen(source)
      data=r.recognize_google(audio)
      print(data)
    return data.lower()
speak("mail is active")


server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("sainishailender0@gmail.com","your app password")
email=EmailMessage()
speak("enter sender details")
while (i!=1):
  try:
   print("from:sainishailender0@gmail.com")
   email["from"]="sainishailender0@gmail.com"
   to=input("to:")
   if("@" not in to  and ".com" not in to):
      speak("plz enter  correct email  address")
      print("plz enter  correct email  address")
      break
     
   email["To"]= to
   speak(" tell the subject")
   sub=mic()
   email["Subject"] =sub
   speak("speak the content" )
   x=mic()
   email.set_content(x)
   speak("can i send this mail")
   res=mic()
   if res == "send":
      server.send_message(email)
      print("message sent successfully")
      server.quit()
   else:
      speak(" Mail is not send" )
      server.quit()
   i=i+1
  except smtplib.SMTPRecipientsRefused:
       speak("email error")
       server.quit()
