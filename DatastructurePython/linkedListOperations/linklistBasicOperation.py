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

    def deleteNode(self,value):
        head = self.root
        while head:
            if self.root.getVal() == value :
                self.root = head.getNext()
                return
            else:
                if head.getVal() == value:
                    tail.setNext(head.getNext())
                    return
                tail = head
                head = head.getNext()
        print "Value not found"

    def searchNode(self,value):
        count = 0
        head = self.root
        while head:
            if head.getVal() == value:
                print "The value is found at index {}".format(count)
                return
            count +=1
            head = head.getNext()

    def display(self):
        head = self.root
        linkedlist = []
        while head:
            linkedlist.append(head.getVal())
            head = head.getNext()
        print "The linkedlist is{} ".format(linkedlist)

    def sizeOf(self):
        head = self.root
        size = 0
        while head:
            size +=1
            head = head.getNext()
        print "The size of linkedlist is {0} ".format(size)

mylinklist = linkedList()
mylinklist.insert(4)
mylinklist.sizeOf()
mylinklist.display()
mylinklist.insert(6,4)
mylinklist.insert(8)
mylinklist.insert(9,6)
mylinklist.insert(9,4)
mylinklist.display()
mylinklist.deleteNode(4)
mylinklist.sizeOf()
mylinklist.display()
mylinklist.searchNode(6)
mylinklist.sizeOf()


