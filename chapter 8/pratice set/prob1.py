#PROBLEM 1
# def greatest(a,b,c):
#     if(a>b and  a>c):
#        return "a"
#     elif(b>a and b>a):
#         return "b"
#     else:
#         return" c "

# print(greatest(1,5,4))
#PROBLEM 2
# def celiustofaranite(celius):
#      f=9/5*(celius+32)
#      return f
# print(celiustofaranite(55))
#PROBLEM 3 
# SUM OF N NATURAL NO
# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + n
# print(sum(4))
#problem 4
# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)
# pattern(3)
#problem 5
l=["Harry","Rohan","Shubham","an"]
def rem(l,word):
    n=[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
print(rem(l,"an"))