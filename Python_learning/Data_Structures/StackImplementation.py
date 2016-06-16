__author__ = 'pallavipriya'

class Stack():

    def __init__(self,limit):
        self.items = []
        self.limit = limit

    def pop(self):
        if len(self.items) < 0:
            print("Stack is empty")
        else:
            temp = self.items[-1]
            self.items = self.items[:-1]
            return temp

    def push(self,value):
        if len(self.items) == self.limit:
            print("The stack is full")
        else:
            self.items.append(value)

    def isStackEmpty(self):
        return  len(self.items) == 0


    def size(self):
        print ("The size of stack is {}".format(len(self.items)))

if __name__ == "__main__":

    s = Stack(10)
    s.push(5)
    s.push(10)
    s.push(2)
    print(s.pop())
    s.push(3)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    s.push(4)
    s.push(14)
    s.push(90)
    s.size()

