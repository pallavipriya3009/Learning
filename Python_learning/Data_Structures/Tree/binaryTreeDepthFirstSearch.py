__author__ = 'pallavipriya'

from StackImplementation import Stack

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

    def depthFirstSearch(self):
        s       = Stack(100)
        visited = []
        head    = self.root
        s.push(head)
        while not s.isStackEmpty():
            if head.getData() not in visited and head.getLeft():
                head = head.getLeft()
                s.push(head)
            else:
                head = s.pop()
                visited.append( head.getData() )
                print (head.getData())
                if head.getRight():
                    head = head.getRight()
                    s.push(head)
        #print( visited )

t = tree()
t.insert(5)
t.insert(9)
t.insert(4)
t.insert(10)
t.insert(1)
t.insert(3)
t.insert(12)
t.depthFirstSearch()



