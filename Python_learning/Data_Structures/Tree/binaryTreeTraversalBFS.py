__author__ = 'pallavipriya'

from queueImplementation import myQueue
class treeNode():

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def getData(self):
        return self.data
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def setData(self,data):
        self.data = data
    def setLeft(self,left):
        self.left = left
    def setRight(self,right):
        self.right = right

class tree():

    def __init__(self):
        self.root = None

    def insert(self,data):

        node = treeNode(data)
        head = self.root
        dir = True
        temp = None
        if not self.root:
            self.root = node
        else:
            while head:
                temp = head
                if data < head.getData():
                    head = head.getLeft()
                    dir = True
                else:
                    head = head.getRight()
                    dir = False
            temp.setLeft(node) if dir else temp.setRight(node)



    def breadthFirstTraverse(self):
        q     = myQueue(100)
        items = []
        q.enqueue(self.root) #insert root
        while not q.isempty():
            head = q.dequeue()
            items.append( head.getData() )
            if head.getLeft():
                q.enqueue(head.getLeft())
            if head.getRight():
                q.enqueue(head.getRight())
        print( items )

t = tree()
t.insert(5)
t.insert(9)
t.insert(4)
t.insert(10)
t.insert(1)
t.insert(3)
t.insert(12)

q1 = t.breadthFirstTraverse()
