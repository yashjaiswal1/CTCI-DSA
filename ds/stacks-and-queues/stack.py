# Implementation of stack using python lists without .append() and .pop()
# ask interviewer if you can use append() & pop() or not and act accordingly
class Stack:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.stack = [None] * self.size

    def push(self, data):
        if(self.top == self.size - 1):
            print("Stack overflow!")
        else:
            self.top += 1
            self.stack[self.top] = data
            print("Item successfully added!")

    def pop(self):
        """
        This function will pop an item out of the stack and return it.
        """
        if(self.top == -1):
            print("Stack underflow!")
        else:
            temp = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return temp

    def peek(self):
        if(self.top == -1):
            print("Stack is empty!")
        else:
            return self.stack[self.top]

    def isEmpty(self):
        return self.top == -1


stk = Stack(3)
print(stk.isEmpty())
stk.pop()
stk.push(10)
stk.push(20)
stk.push(30)
stk.push(40)
print(stk.peek())
print("Popped value = " + str(stk.pop()))
print("Popped value = " + str(stk.pop()))
print("Popped value = " + str(stk.pop()))
stk.pop()
stk.isEmpty()
stk.peek()
