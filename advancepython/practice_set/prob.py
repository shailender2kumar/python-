try:
 with open ("file1.txt") as f:
      Print(f.read())
except Exception as e:
      print(e)
try:
  with open("file2.txt") as f:
      Print(f.read())
except Exception as e:
     print(e)
try:
  with open ("file3.txt") as f:
     print(f.read())
except Exception as e:
     print(e)
finally:
    print("final")
