class Stack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def isEmpty(self):
        return len(self.__stack) == 0

    def isFull(self):
        return len(self.__stack) == self.__capacity

    def push(self, item):
        if self.isFull():
            raise Exception("Stack is full")
        else:
            self.__stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.__stack.pop()
        else:
            raise Exception("Stack is empty")

    def top(self):
        if not self.isEmpty():
            return self.__stack[-1]
        else:
            raise Exception("Stack is empty")

stack1 = Stack(5)

stack1.push(1)
stack1.push(2)
print(stack1.isFull())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.isEmpty())

class Base:
    def __init__(self):
        self.a = "Base"
    
    def display(self):
        return self.a

class Derived(Base):
    def __init__(self):
        super().__init__()
        self.a = "Derived"
    
    def display(self):
        return self.a + " " + super().display()

d = Derived()  # Fixed instantiation
print(d.display())  # Fixed function call
