spam1='make a lot of money'
spam2=" buy now"
spam3 = "suscribe this "
spam4 = " click this "
message=input("enter in message")
if((spam1 in message) or (spam2 in message) or (spam3 in message) or (spam4 in message)):
    print("this message is spam")
else:
    print("this message is not spam")