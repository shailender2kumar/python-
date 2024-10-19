class class1:
    def __init__(self):
        print("Contructor of class1")
    def prin(self):
        print("class1")

class class2(class1):
    def __init__(self):
        print("Contructor of class2")
    def class2(self):
          print("class2")

class class3(class2):
    def __init__(self):
        super().__init__() #parent  ka constructoer chalega
        print("Contructor of class3")
    def class3(self):
          print("class3")
# c1=class1()
c3=class3()