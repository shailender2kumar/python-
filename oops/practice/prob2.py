class Calculator:
     def square(self,n):
         x=n*n
         return x
     def cube(self,n):
         x=n*n*n
         return x
     def squareroot(self,n):
         x=n**0.5
         return x
y=Calculator()
print(y.square(5))
print(y.squareroot(25))