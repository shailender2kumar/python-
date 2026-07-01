class Student:
      college_name = 'ABC College'
      name = "anonymous"
    #default constructors
      def __init__(self):
         pass
         #paramaterized constructor
      def __init__(self,fullname,marks):
        self.name = fullname  # obj attr >class attr
        self.marks = marks
        print( "constructer called")
        # name = "karan kumar"
      @staticmethod
      def hello():
        return f"welcome Student"
s1 = Student("karan",97)
print(s1.name,Student.hello())
s2 = Student("arjun",44)
print(s2.name,s2.marks,s2.college_name)



# print(s1.name)
# print(s1.name)
# class Car:
#     color = "blue"
#     brand = "suzuki"
# car1 = Car()
# print(car1.color)

 #Class.attr com
 #Obj.attr


class Student:
    def __init__(self,marks1,marks2,marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    
    def average(self):
        return f"{(self.marks1+self.marks2+self.marks3)/3}"

s6 = Student(1,2,3)
print(s6.average())


