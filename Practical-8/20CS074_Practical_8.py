class Stack(object):
    def __init__(self, size):
        self.index = []
        self.size = size

    def push(self, data):
        ''' Pushes a element to top of the stack '''
        if (self.isFull() != True):
            self.index.append(data)
            print("Element Pushed.")
        else:
            print('Stack overflow')

    def pop(self):
        ''' Pops the top element '''
        if (self.isEmpty() != True):
            print("Element Poped")
            return self.index.pop()
        else:
            print('Stack is already empty!')

    def isEmpty(self):
        ''' Checks whether the stack is empty '''
        return len(self.index) == []

    def isFull(self):
        ''' Checks whether the stack if full '''
        return len(self.index) == self.size

    def stackSize(self):
        ''' Returns the current stack size '''
        return len(self.index)

    def __str__(self):
        myString = ' '.join(str(i) for i in self.index)
        return myString

    def traversal(self):
        print("\nTraversal :- ",self,"\n")

if __name__ == '__main__':
    st = Stack(10)

    st.push(10)
    st.push(20)
    st.push(30)
    st.push(50)
    st.push(40)
    st.push(100)
    st.push(60)
    st.push(90)
    st.traversal();

    st.pop()
    st.pop()
    st.pop()

    st.traversal()

    print("\nID : 20CS074.")
    print("\nName : Mandar Sanghavi.")
