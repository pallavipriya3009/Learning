__author__ = 'pallavipriya'

#To calculate the perimeter of a polygon
import math

class point():

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self,p2):
        return math.sqrt((p2.x - self.x) ** 2 + (p2.y - self.y) ** 2)

class polygon():

    def __init__(self):

        self.vertices = []

    def add_point(self,point):
        self.vertices.append((point))

    def perimeter(self):
        perimeter = 0
        points = self.vertices + [(self.vertices[0])]
        for itr in range(len(self.vertices)):
            perimeter += points[itr].distance(points[itr + 1])

        print ("The perimeter of the polygon is {}".format(perimeter))

p = polygon()
p.add_point(point(5,1))
p.add_point(point(3,2))
p.add_point(point(4,3))
p.add_point(point(1,1))
p.perimeter()

print(isinstance(p,object))

