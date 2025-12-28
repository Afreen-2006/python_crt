class Employee:
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary
class Manager(Employee):
    def display(self):
        print(f"Manager:{self._name},salary:{self._salary}")
emp=Manager("alice",70000)
emp.display()