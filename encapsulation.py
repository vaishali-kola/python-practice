class Student:
    def __init__(self):
        self.__marks=95#private variable
    def get__marks(self):#to get the value
        return self.__marks
    def set__marks(self,v):#to change the value
        self.__marks=v
s=Student()#object is created
print(s.get__marks())#marks are printed
s.set__marks(100)#marks changed
print(s.get__marks())#again printed

        