# Day 61: Create a program to implement a stack using a list.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None

    def size(self):
        return len(self.items)


# Example:
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack size:", stack.size())
    print("Top of stack:", stack.peek())

    item = stack.pop()
    print("Popped item:", item)

    stack.push(5)

    print("Stack size:", stack.size())
    print("Top of stack:", stack.peek())

    item = stack.pop()
    print("Popped item:", item)

    print("Stack size after popping:", stack.size())