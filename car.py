class car:
    def __init__(self,name,color):
       self.name=name
       self.color=color
    def show(self):
       print("name:",self.name)
       print("color:",self.color)
m1=car("maruti suzuki","black")
m1.show()
