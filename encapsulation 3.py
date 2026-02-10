class Employee:
    def __init__(self):
        self._salary=50000
    def get_salary(self):
        return self._salary
    def set_salary(self,v):
        self._salary=v
s1=Employee()
print(s1.get_salary())
s1.set_salary(75000)
print(s1.get_salary())
