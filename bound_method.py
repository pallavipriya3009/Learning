__author__ = 'pallavipriya'

class test1():

    @classmethod
    def clsmethod(cls,n):
        print ("I am in class method",n)

    def insmethod(self,n):
        print("I am instance method",n)

    @staticmethod
    def method(n):
        print ("I am static method",n)


t = test1()
m1 = t.insmethod
print(m1)
m1(7)

test1.clsmethod(8)
print(test1.clsmethod)

test1.method(6)
print(test1.method)