l=[1,2,3,4,5,6,7,8,9,10]
n=int(input("enter "))
table=[n*i for i in l]
print(str(table))
with open ("table.txt","w") as f:
     f.write(str(table))