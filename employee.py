class Employee:
    def __init__(self,id,salary):
        self.id=id
        self.salary=salary
    def show(self):
        print("id:",self.id)
        print("salary:",self.salary)
e1=Employee(111,50000)
e1.show()