a=int(input("enter the number"))
b= int(input("enter second number"))

if(b==0):
    raise ZeroDivisionError("Hey our Program is not meant to number by zero")
else:
  print(f"The division a/b is {a/b}")