__author__ = 'pallavipriya'

class myQueue():

    def __init__(self,limit):
        self.item = []
        self.limit = limit

    def enqueue(self,value):
        if len(self.item) < self.limit :
            self.item.append(value)
        else:
            print("the queue is full")

    def dequeue(self):
        temp = self.item[0]
        self.item = self.item[1:]
        return temp

    def isfull(self):
        return len(self.item) == self.limit

    def isempty(self):
        return len(self.item) == 0

    def queueItems(self):
        for itr in self.item:
            print (itr)

    def size(self):
        return len(self.item)

q = myQueue(4)

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
q.dequeue()
q.enqueue(5)

#q.queueItems()



