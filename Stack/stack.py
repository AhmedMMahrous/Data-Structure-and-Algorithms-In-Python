from sympy import re


class stack:
    def __init__(self):
        self.s=[]

    #insert a new element to the end of the stack
    def push(self,value):
        self.s.append(value)

    #remove the last element
    def pop(self):
        self.s.pop()

    #check if stack is empty or not
    def isEmpty(self):
        if len(self.s)==0:
            return True
        else:
            return False
        
    def Top(self):
        if self.isEmpty():
            print("Eroor")
        else:
            return self.s[-1]

stack1=stack()
stack1.push(2)
stack1.push(4)
stack1.push(6)
print(stack1.Top())
stack1.pop()
print(stack1.Top())
stack1.pop()
stack1.pop()
print(stack1.Top())
