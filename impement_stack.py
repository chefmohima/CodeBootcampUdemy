class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
            return
        item = self.stack.pop()
        return item

    def peek(self):
        if self.is_empty():
            print('Stack is empty')
            return
        return self.stack[-1]


# Test
test_stack = Stack()
print(test_stack.is_empty())        # True
test_stack.push(1)
test_stack.push(2)
test_stack.push(3)
print(test_stack.is_empty())        # False
print(test_stack.peek())            # 3
print(test_stack.pop())             # 3
print(test_stack.peek())                   # 2

