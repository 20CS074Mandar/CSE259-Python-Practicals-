from abc import  ABCMeta,abstractmethod

#Singleton design pattern

#In singleton , we have a class and this class can only have one instance

#so if we have for example  a class person here we can only have one person object
class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def print_data(self):
        """implement in child class"""

#here we are inheriting from the Iperson to implement the singleton pattern
class PersonSingleton(IPerson):

    __instance=None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance==None:
            print("Error no instance found , don't worry creating One")
            PersonSingleton("Default Name",0)
        return PersonSingleton.__instance

#this constructor cannot be used multiple times becaue this will override the instance
    def __init__(self,name,age):
        if PersonSingleton.__instance !=None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.name=name
            self.age=age
            PersonSingleton.__instance=self

    @staticmethod
    def print_data():
        print(f"Name :{PersonSingleton.__instance.name},Age :{PersonSingleton.__instance.age}")

p=PersonSingleton("Ram",30)
print(p)
p.print_data()

#In this it wil raise exception that we can't create an another object of the same class
p2=PersonSingleton("Shyam",20)
print(p2)
p2.print_data()

p3=PersonSingleton.get_instance()
print(p3)
p3.print_data()
