__author__ = 'Wiktor'

from random import shuffle


class Tour(object):
    distance = 0

    def __init__(self,tourManager):
            self.tourManager = tourManager
            self.tour = []
            self.random = shuffle

    def getTour(self):
        return self.tour

    def getCity(self,tourPosition):
        return self.tour[tourPosition]

    def setCity(self,tourPosition,city):
        self.tour.insert(tourPosition,city)
        self.distance = 0

    def generateIndividual(self):
        for cityIndex in range(0,self.tourManager.numberOfCities()):
            self.setCity(cityIndex,self.tourManager.getCity(cityIndex))
        self.random(self.tour)



    def tourSize(self):
        return len(self.tour)

    def getDistance(self):
        if self.distance == 0:
            tourDistance = 0
            for cityIndex in range(0,self.tourSize()):
                fromCity = self.getCity(cityIndex)
                if (cityIndex+1 < self.tourSize()):
                    destinationCity = self.getCity(cityIndex+1)
                else:
                    destinationCity = self.getCity(0)
                tourDistance += fromCity.distanceTo(destinationCity)
            distance = tourDistance
        return distance


    def __str__(self):
        geneString = ""
        for i in range (0,self.tourSize()):
            geneString += str(self.getCity(i))+"|"
        return  geneString










