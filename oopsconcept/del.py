# del  
#used to delete object properties or object itself

class Student:
      def __init__(self,name):
            self.name = name 
s1 = Student("shradha")
print(s1.name)
del s1
print(s1.name)

class Account:
      def __init__(self,acc_no,acc_pass):
            self.acc_no = acc_no
            self.__acc_pass = acc_pass # make it private it can access  from  class nt outside class

acc1 = Account("123456","abcde")
print(acc1.acc_no)
print(acc1.__acc_pass)

class Person :
      __name = "anonymos"

      def __hello(self):
            print("hello  person!")
s1 = Person()
print(s1.__hello)

#Inheritance
class Car:
    @staticmethod
    def start():
          print("car started...")
    
    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self, name):
         self.name = name


car1 = ToyotaCar("fortuner")
car2=ToyotaCar("pirus")
print(car1.name)
car1.start()

#multi-level inhertance  
class Car:
    @staticmethod
    def start():
          print("car started...")
    
    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self, brand):
         
         self.brand = brand
         print(f"{brand}") 

class Fortuner(ToyotaCar):
     def __init__(self,type):
          self.start()
          super().__init__("Toyota")
          self.type = type
          print(f"{type}")


F1 = Fortuner("diesel")

#Multiple INHERITANCE
class A:
     varA = "welcome to class A "
class B:
     varB = "welcome to class B"
class C(A,B):
     varC =  "welcome to class C"  

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

      
