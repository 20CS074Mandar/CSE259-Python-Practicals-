#class student,exam,result

class Student:
    def __init__(self,rollno,name,division):
        self.name=name
        self.rollno=rollno
        self.divison=division
    def getStudent(self):
        print("Name : ",self.name)
        print("Roll No : ",self.rollno)
        print("Division : ",self.divison)

class Exam(Student):


    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks

class Result(Exam):

    def getTotalMarks(self):
        Total_Marks=sum(self.getMarks())
        return Total_Marks


Mandar=Result(74,"Mandar",2)
print("\nStudent Information : ")
Mandar.getStudent()
Mandar.setMarks([10,20,30,40,50,60])
print("Total Marks :- ",Mandar.getTotalMarks())



print("\nId : 20CS074 ")
print("Name : Mandar Sanghavi\n")

