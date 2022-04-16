
import  math
#Implementing Arithmetic Error
def ArithmeticEr():
    try:
        a = 10 / 0
        print(a)
    except ArithmeticError:
        print("This statement is raising an arithmetic exception.")
    else:
        print("Success.")


#Implementing Exception Lookup Error

def LookUpEr():
    try:
        a = [1, 2, 3]
        print(a[3])
    except LookupError:
        print("Index out of bound error.")

#Implementing Floating Error

def FloatingEr():
    print(math.exp(1000))

#Implementing Index Error
def IndexEr():
    array = [0, 1, 2]
    print(array[3])



    ArithmeticEr()
    # LookUpEr()
    # FloatingEr()
    # IndexEr()