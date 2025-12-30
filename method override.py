'''methodoverride'''

class methodoverride1:
    def display(self):
        print("method invoked from base class")
class methodoverride2(methodoverride1):
    def display(self):
        print("method invoked from derived class")
ob=methodoverride2()
ob.display()