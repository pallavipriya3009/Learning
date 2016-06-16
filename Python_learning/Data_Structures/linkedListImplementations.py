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


    def insert(self,value,after=None):

        if not self.next:
            node = linkedList(value)
            self.next = node

        else:
            head = self.next
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
        head = self.next
        while head:
            print(head.getValue())
            head = head.getNext()

    def deleteItem(self,value):
        head = self.next

        while head.getNext():
            if head.getNext().getValue() == value:
                head.setNext(head.getNext().getNext())
            head = head.getNext()


#print (head.getValue())
l = linkedList()
l.insert(5)
l.insert(6)
l.insert(3,5)
l.insert(7,5)

l.traverse()
l.deleteItem(7)
print('deleted')
l.traverse()







