with open("this.txt") as f:
    read=f.read()
with open("copy.txt","w") as g:
     g.write(read)