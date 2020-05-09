# --- Directions
# Implement a Queue datastructure using two stacks.
# *Do not* create an array inside of the 'Queue' class.
# Queue should implement the methods 'add', 'remove', and 'peek'.
# For a reminder on what each method does, look back
# at the Queue exercise.
# --- Examples
#     q = Queue();
#     q.add(1);
#     q.add(2);
#     q.peek();  # returns 1
#     q.remove(); # returns 1
#     q.remove(); # returns 2

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


class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, item):
        # all enqueues in s1
        self.s1.push(item)

    def dequeue(self):
        if self.s1.is_empty():
            print('Empty stack')
            return None
        # move all items from s1 to s2
        # we need to get the first item that was inserted
        while self.s1.is_empty() == False:
            self.s2.push(self.s1.pop())
        item = self.s2.pop()
        # restore s1 first
        while self.s2.is_empty() == False:
            self.s1.push(self.s2.pop())
        return item

    def peek(self):
        if self.s1.is_empty():
            print('Empty stack')
            return
        while self.s1.is_empty() == False:
            self.s2.push(self.s1.pop())
        item = self.s2.stack[-1]
        while self.s2.is_empty() == False:
            self.s1.push(self.s2.pop())
        return item


# Tests
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.peek())         # 1
print(q.dequeue())      # 1
print(q.peek())         # 2
    