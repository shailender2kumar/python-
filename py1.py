# print("hello world")

def func():
    x= 5+7
    print(x) 

func()
# name ="Shradha"
# age = 22
# print(age)
# print("hello world")

# first_name = 'tony Stark'
# Age = 51
# isGenius = True 
# name  = input("what is your name ")
# print("hello " +name)
# nam1 = input('who is your superhero')
# print(nam1)
# old_age = int(input("enter your old age"))
# new_age = int(old_age) + 2
# print(new_age)
# float()
# str()
# bool()
# first = input("enter first number")
# second = input("enter second number")
# sum =  int(first) + int(second)
# print("the sum is : " +str(sum))

#String
name = 'Tony Stark '
# print(name.upper())  
# print(name.lower())# doesn't effect original  string   gives   me   new string
# print(name.find('stark'))
# print(name.replace('Tony Stark', "Ironman"))
print('T'in  name)

#airthmatic 
print(5/2)
print(5//2) #for  floor division
print(5 % 2) #gives reminder
print(5 ** 2) #  gives 5^2

i =5 
i=i+2
result = 2+3*5
print(result)
# here is a comment
print(3>2)
print(3 == 3)
print(3 != 3)
print(2>3 or 2>1)
print(2<3 and 1>2)
print(not 1>3)
age = 19 
if age >= 18:
    print("you are adult")
elif age < 18 and age > 3:
     print("you are in school")

first = int(input("enter  first number"))
operator = (input("enter operator(+,-,*,/,%) : "))
second =int(input("enter second number"))

if operator == '*':
    print(first * second)
elif operator =='+':
    print(first + second)
elif operator == '-':
    print(first - second)
elif operator == '/':
    print(first / second)
elif operator == '%':
    print(first % second)
else:
    print("invalid form")


numbers = range(5) # 0,1,2,3,4
print(numbers)
i=1
while(i<5):
     print(i)
     i=i+1
i=1
while i <= 5 :
      print(i * "*")
      i=i+1
# for loops
for i in range(0,5):
    print(i+1)

marks=[2,2,4,6,7]
# print(marks[0:4])
# marks.append(99)
# marks.insert(0,22)
i=0
while(i<len(marks)):
    print(marks[i])
    i=i+1
marks.clear()
print(marks)
students= ["ram","shyam","kishan", "radha","radhika"]
for student in students:
    if student == "radha":
        break;
    print(student)

marksTuple=(4,4,5,3,2)
#marksTuple[0]=( 2)
print(marksTuple.index(4))
print(marksTuple.count(4))

#set
marks={95,98,97,97}
for score in marks:
    print(score)
marks = {
    "english" : 95,
    "chemistry" : 33
}
marks["chemistry"]= 21
print(marks)

import math
print((math))


def fun():
    sum = 5+4
    print(sum)

print(fun())



