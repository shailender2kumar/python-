class Employee:
    company= "ITC"
    def show(self,name,salary):
        print(f"name {name} salary {salary}")
class Raju:
    def ral(self):
          print("Raju")


class Programmer(Employee,Raju):
      name=""
      language=" "
      company="Itc"
      def showLanguage(self,name,language):
        print(f"the name{self.name}and good {self.language} language")
      

E=Employee()      

b=Programmer()
print(b.show("ra",1234))
print(E.show("ram",1234))
print(b.ral())
