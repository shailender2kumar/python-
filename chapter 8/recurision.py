def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
      x = n*factorial(n-1)
      return x 
print(factorial(2))