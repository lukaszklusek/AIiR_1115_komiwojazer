__author__ = 'Wiktor'

import random
import math


class City(object):
    def __init__(self, x= None,y=None):
        if x is None:
            self.x = random.randint(0,200)
        else:
            self.x = x
        if y is None:
            self.y = random.randint(0,200)
        else:
            self.y=y


    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceTo(self,city):
        xDistance = math.fabs(self.getX() - city.getX())
        yDistance = math.fabs(self.getX() - city.getX())
        return math.sqrt(xDistance**2 + yDistance**2)




# city = City()
#
# city2 = City()
#
# print(city)
# print(city2)
#
# print("Distance from first city to second city equals")
# print(city.distanceTo(city2))
