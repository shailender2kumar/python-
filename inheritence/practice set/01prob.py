class TwoDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"{self.i}i+{self.j}j")
class ThreeDVector(TwoDVector):
       def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
       def show(self):
        print(f"{self.i}i+{self.j}j+{self.k}k")
a=TwoDVector(1,2)
b=ThreeDVector(3,3,3)
b.show()
