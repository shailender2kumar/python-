from random import  randint
class Train :
       def __init__(slf,trainNo):
         slf.TrainNo=trainNo
       def BookTicket(self,fro,to):
          print(f"Ticket is booked in train no :{trainNo} from {fro} to {to}")
       def GetStatus(self,trainNo):
        print(f"Train no:{ trainNo} is running on time")
       def getFare(self,trainNo,fro,to):
        print(f"Ticket fare in train no :{trainNo} from {fro} to {to} is {randint(222,5555)}")
        
tr=Train(12111)
tr.BookTicket(110034,"rewari","goa")
tr.GetStatus(110034)
tr.getFare(110045,"rewari","goa")
#we can  rename self parameter  to any name