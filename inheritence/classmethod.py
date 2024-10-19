#class method you can excess  class attribute not object attribute
class Empl:
    a=1
    @classmethod
    def show(cls):
        print(f"the attribute{cls.a}")
        
o=Empl()
o.a = 2
o.show()
