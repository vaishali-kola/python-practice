class student:
    def __init__(self,name,roll,branch):
        self.name=name
        self.roll=roll
        self.branch=branch
    def show(self):
        print(self.name)
        print(self.roll)
        print(self.branch)
s1=student("vaishali",11,"cse")
s1.show()