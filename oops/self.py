class employee:
    language ="Python"
    salary="jat"
    @staticmethod
    def greeet():
        print("good Morning")
    def getinfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")

harry=employee()
harry.language="JavaScript"
# print(harry.getinfo())
print(harry.greeet())
