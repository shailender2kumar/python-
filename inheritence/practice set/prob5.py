class Vector:
      def __init__(self,i,j,k):
          self.i=i
          self.j=j
          self.k=k
      def __add__(self,ima):
         return Vector(self.i+ima.i,self.j+ima.j,self.k+ima.k)

      def show(self):
        print(f"{self.i}i + {self.j}j+ {self.k}k")

v=Vector(2,3,4)
v1=Vector(4,7,6)
v2=v+v1
v2.show()