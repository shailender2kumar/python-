from random import randint

i=0
n=randint(1,10)
a=int()
while(a!=n):
   a=int(input("Guess the Number  "))
   if(a>n):
    print("Guess the smller")
    i=i+1
   elif(a<n):
        print("Guess the Largest")
        i=i+1
   else:
        print(f"you correctly guess this number {n} in {i} attempt")


