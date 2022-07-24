class queue:
    def __init__(self):
        self.q = []

    def enqueue(self,value):
        self.q.append(value)

    def dequeue(self):
        self.q.pop(0)

    def front(self):
        return self.q[0]

queue1 = queue()
queue1.enqueue(2)
queue1.enqueue(4)
queue1.enqueue(6)
print(queue1.front())
queue1.dequeue()
print(queue1.front())
