f=open("file.txt")
line=f.readline() #it return a list of lines
# print(lines)
while(line!=" "):
    print(line.strip())
    line= f.readline()
f.close()

