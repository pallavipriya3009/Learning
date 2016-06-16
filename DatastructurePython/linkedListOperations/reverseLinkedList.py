__author__ = 'pallavipriya'

class node(object):

    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

    def getNext(self):
        return self.next

    def setNext(self,next):
        self.next = next

    def setVal(self,value):
        self.value = value

    def getVal(self):
        return self.value

class linkedList(object):

    def __init__(self):
        self.root = None

    def insert(self,value,after=None):
        head = self.root
        Node = node(value)

        if not self.root:
            self.root = Node
        else:
            while head.getNext():
                if head.getVal() == after:
                    Node.setNext(head.getNext())
                    head.setNext(Node)
                    return
                head = head.getNext()
            head.setNext(Node)

    def reverseLinkedList(self):
        head = self.root
        previous = None
        while head:
            current = head
            head = head.getNext()
            current.setNext(previous)
            previous = current
        self.root = previous

    def display(self):
        head = self.root
        linkedlist = []
        while head:
            linkedlist.append(head.getVal())
            head = head.getNext()
        print "The linkedlist is{} ".format(linkedlist)

mylinklist = linkedList()
mylinklist.insert(4)
##mylinklist.display()
mylinklist.insert(6,4)
mylinklist.insert(8)
mylinklist.insert(9,6)
mylinklist.insert(9,4)
#mylinklist.sizeOf()
mylinklist.display()
mylinklist.reverseLinkedList()

#mylinklist.sizeOf()

mylinklist.display()
