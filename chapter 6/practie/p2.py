marks1= int(input("Enter Marks 1: "))
marks2 = int(input("enter Marks 2 : "))
marks3 = int(input("Enter Marks 3 :"))

total_percentage = (marks1+ marks2+marks3)/300
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>= 33):
    print("You are pass")
else:
    print("You failed, try next year:", total_percentage)