# Lafore
# Reverse a string using a stack

class Stack:

    def __init__(self):
        self.top = -1
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        # print("Item added.")
        self.top += 1

    def pop(self):
        if(self.top == -1):
            print("Stack underflow!")
            return None
        else:
            # print("Item removed.")
            self.top -= 1
            return self.stack.pop()

    def peek(self):
        return self.stack[self.top] if self.top > -1 else "Stack is empty."


main_stack = Stack()
while(1):
    input_str = input("Enter the string to be reversed :")
    if input_str == "quit()":
        print("Exiting...")
        break
    parsed_str = list(input_str.strip())
    for i in parsed_str:
        main_stack.push(i)

    for i in range(len(parsed_str)):
        print(main_stack.pop())
