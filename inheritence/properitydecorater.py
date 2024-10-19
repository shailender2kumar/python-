class nami:
      @property
      def name(self):
          return f"{self.fname} {self.lname}"
      @name.setter
      def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

e=nami()  
e.name= "haary khan"
print(e.fname,"naa",e.lname)