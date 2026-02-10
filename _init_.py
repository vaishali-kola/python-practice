class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name)
        print(self.age)
s1=student("vaishali",19)
s1.show()