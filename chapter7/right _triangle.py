n= 5
# for i in range(0,n):
#     print(" "*(n-i), end=" ")
#     print("*"*(i+1), end=" ")
#     print()
# for i in range(0,n):
#      print("*"*(n-i), end=" ")
#      print(" "*(i+1), end=" ")
#      print()
# for i in range(0,n):
#      print(" "*(i), end=" ")
#      print("*"*(n-i), end=" ")
#      print()
 
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-3),end="")
        print("*",end=" ")
        print("*",end=" ")
    print("")