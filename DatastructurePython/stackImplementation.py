__author__ = 'pallavipriya'

class stack(object):

    def __init__(self):
        self.data = []

    def push(self,value):
        self.data.append(value)

    def pop(self):
        if len(self.data) == 0:
            print "The stack is empty"
        else:
            x = self.data[-1]
            self.data = self.data[:-1]
            return x

    def display(self):
        print self.data

    def isStackEmpty(self):
        return self.data == 0

testStack = stack()
testStack.push(5)
testStack.push(6)
testStack.push(9)
testStack.pop()
testStack.push(4)
testStack.pop()
testStack.display()
print "is stack is empty?",testStack.isStackEmpty()
