class employee:
    language ="Python"
    salary="jat"
    def __init__(self): #dunder method  which is automatically called
        print("Dunder")
    @staticmethod
    def greeet():
        print("good Morning")
    def getinfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")
harry= employee()