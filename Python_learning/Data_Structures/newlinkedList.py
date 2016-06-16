__author__ = 'pallavipriya'

class linkedList():

    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setNext(self,next):
        self.next = next

    def setValue(self,value):
        self.value = value



class operation():

    def __init__(self):
        self.root = None

    def insert(self,value,after=None):
        head = self.root
        if not head:
            node = linkedList(value)
            self.root = node
        else:
            node = linkedList(value)
            if after:
                while head:
                    if head.getValue() == after:
                        node.setNext(head.getNext())
                        head.setNext(node)
                    head = head.getNext()
            else:
                head.setNext(node)


    def traverse(self):
        head = self.root
        while head:
            print(head.getValue())
            head = head.getNext()

    def deleteItem(self,value):
        head = self.root

        while head.getNext():
            if head.getNext().getValue() == value:
                head.setNext(head.getNext().getNext())
            head = head.getNext()

o = operation()
o.insert(5)
o.insert(6)
o.insert(3,5)
o.insert(7,5)

o.traverse()
o.deleteItem(7)
print('deleted')
o.traverse()







