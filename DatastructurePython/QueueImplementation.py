__author__ = 'pallavipriya'
class queue(object):

    def __init__(self):
        self.data = []

    """def enque(self,value):
        self.data.append(value)
        return self.data """

    def enque(self,valuelist):
        self.data.extend(valuelist)
        return self.data

    def deque(self):
        if self.isempty():
            print "No data in the queue "
        else:
            x = self.data[0]
            self.data = self.data[1:]
            return x

    def display(self):
        print self.data

    def isempty(self):
        return len(self.data) == 0

Queue1 = queue()
print Queue1.enque([4,5,6])
print Queue1.deque()
print Queue1.deque()
print Queue1.enque([3,6])
print "if Queue is empty?",Queue1.isempty()

