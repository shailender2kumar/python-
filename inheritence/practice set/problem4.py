class complex:
     def __init__(self,real,imaginery):
         self.real=real
         self.imaginery=imaginery
     
     def show(self):
        {
        print(f"{self.real}+{self.imaginery}j")
     }
     def __add__(self,ima):
        return complex(ima.real+self.real ,ima.imaginery+self.imaginery)

c=complex(2,3)
c1=complex(4,5)
c2=c+c1
c2.show()