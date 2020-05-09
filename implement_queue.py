# --- Description
# Create a queue data structure.  The queue
# should be a class with methods 'add' and 'remove'.
# Adding to the queue should store an element until
# it is removed
# --- Examples
#     const q = new Queue();
#     q.add(1);
#     q.remove(); # returns 1;


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
            return
        return self.queue[0]

# Tests
test_queue = Queue()
print(test_queue.is_empty())    # True
test_queue.enqueue(1)
test_queue.enqueue(2)
test_queue.enqueue(3)
print(test_queue.queue)         # [1,2,3]
print(test_queue.peek())        # 1
print(test_queue.queue)         # [1,2,3]
print(test_queue.dequeue())     # 1
print(test_queue.queue)         # [2,3]
