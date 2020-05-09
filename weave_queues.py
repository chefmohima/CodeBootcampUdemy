# Weave 2 queues q1 and q2 into one queue
# so that the result queue has alternate elements from q1 and q2
# if q1 = [1, 2, 3] and q2 = [10, 20, 30, 50]
# then result queue = [1,10,2,20,3,30,50]


class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)
        return

    def dequeue(self):
        if self.is_empty():
            print('Nothing to dequeue')
            return
        first_item = self.queue.pop(0)
        return first_item

    def peek(self):
        if self.is_empty():
            print('queue is empty')
            return False
        return self.queue[0]

    def print_queue(self):
        print(self.queue)


def weave(q1, q2):
    q3 = Queue()
    while q1.peek() and q2.peek():
        q3.enqueue(q1.dequeue())
        q3.enqueue(q2.dequeue())
    while q1.peek():
        q3.enqueue(q1.dequeue())
    while q2.peek():
        q3.enqueue(q2.dequeue())
    q3.print_queue()

q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)

q2 = Queue()
q2.enqueue(10)
q2.enqueue(20)
q2.enqueue(30)
q2.enqueue(50)
# Tests
weave(q1, q2)
