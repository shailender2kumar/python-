'''
1 for snake
-1 for water
0 for gun
'''
computer = -1
your = input("enter your choice")
youDict= {"s":1,"w":-1,"g":0}
you = youDict[your]
if(computer== -1 and you == 1):
    print("You win ")
elif(computer== -1 and you == 0):
    print("You lose ")
if(computer== -1 and you == -1):
    print("You wins ")
elif(computer== -1 and you == 0):
    print("You lose ")
