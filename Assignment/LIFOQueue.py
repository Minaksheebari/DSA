from queue import Queue

class StackUsingQueues:
    def __init__(self):
        self.main_queue = Queue()
        self.temp_queue = Queue()

    def push(self, element):
        self.temp_queue.put(element)

        while not self.main_queue.empty():
            self.temp_queue.put(self.main_queue.get())

        self.main_queue, self.temp_queue = self.temp_queue, self.main_queue

    def pop(self):
        if not self.empty():
            return self.main_queue.get()
        else:
            raise IndexError("Stack is empty")

    def top(self):
        if not self.empty():
            return self.main_queue.queue[0]
        else:
            raise IndexError("Stack is empty")

    def empty(self):
        return self.main_queue.empty()

stack = StackUsingQueues()
stack.push(10)
stack.push(8)
stack.push(6)

print("Top:", stack.top())  
print("Pop:", stack.pop())  
print("Pop:", stack.pop())  
print("Empty:", stack.empty())  
