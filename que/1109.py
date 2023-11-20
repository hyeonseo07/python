class CircularQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.list=[None]*capacity
        self.front=0
        self.rear=0

    def isEmpty(self):
        if self.rear == self.front:
            return True
        return False
    
    def isFull(self):
        if self.front==(self.rear+1)%self.capacity:
            
    
    def enqueue(self, item):

    def dequeue(self):