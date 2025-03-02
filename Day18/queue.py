class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def isFull(self):
        return len(self.queue) == self.capacity
    
    def enqueue(self, item):
        if self.isFull():
            raise Exception("Queue is full")
        else:
            self.queue.append(item)
            
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        else:
            return self.queue.pop(0)
        
    def front(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        else:
            return self.queue[0]
        
queue1 = Queue ( capacity =5)

queue1 . enqueue (1)

queue1 . enqueue (2)

print( queue1 . isFull ())

print ( queue1 . front () )
print ( queue1 . dequeue () )

print ( queue1 . front () )
print ( queue1 . dequeue () )
print ( queue1 . isEmpty () )

   