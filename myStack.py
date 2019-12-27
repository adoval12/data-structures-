### Alex Doval
### here is an implenetation of stack

class mystack:
    def __init__(self):
        self.stack = []

    "push() inserts an item into the stack"   
    def push(self, x):
        self.stack += [x]

    "pop() takes the top item in the stack and returns it"    
    def pop(self):
        if len(self.stack) == 0:
            print("cannot pop the stack because there is nothing in it")
        else:
            return self.stack.pop()

    "peek() returns the top item in the stack"
    def peek(self):
        if len(self.stack) == 0:
            print("cannot peek the stack because there is nothing in it")
        else:
            peek = len(self.stack) - 1
            return self.stack[peek]
    
    "returns the length of the stack"    
    def length(self):
        return len(self.stack)
    
    def printStack(self):
        printStack = "|"
        line = "---"
        for i in range(len(self.stack)):
            line += "----"
            if i == (len(self.stack) - 1):
                printStack += " " + str(self.stack[i])
            else:
                printStack += " " + str(self.stack[i]) + " |"
        print(line)
        print(printStack)
        print(line)


                
            
        
