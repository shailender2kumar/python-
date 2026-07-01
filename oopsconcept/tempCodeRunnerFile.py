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