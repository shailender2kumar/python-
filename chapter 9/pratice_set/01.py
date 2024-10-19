f=open("poem.txt")
content= f.read()
if("Twinkle" in content):
   print("present")

f.close()