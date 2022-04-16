# Defining parent class
class Parent():

    # Constructor
    def __init__(self):
        self.value = "Inside Parent"

    # Parent's show method
    def show(self):
        print(self.value," accessing of parent class")


# Defining child class
class Child(Parent):

    # Constructor
    def __init__(self):
        self.value = "Inside Child"

    # Child's show method
    def show(self):
        print(self.value," accessing show of child class")


# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()

print("\nId : 20CS074")
print("Name : Mandar Sanghavi")
