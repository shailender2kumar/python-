# with open("log.txt") as f:
#     content =f.read()

#     if("python" in content):
#         print(" yes")
#     else:
#        print("no")

    
with open("log.txt") as f:
    lines =f.readlines()

lineno=1
for line in lines:
    if("python" in line):
        print(f" yes: {lineno}")
    else:
       print("no") 
       lineno+= 1

    