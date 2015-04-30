__author__ = 'Wiktor'

from TSP_SA.City import City

class TourManager(object):

    def __init__(self):
        self.destinationCities = []

    def getDestinationCity(self,i):
        return self.destinationCities[i]

    def setDestinationCity(self,i,destinationCity):
        self.destinationCities[i] = destinationCity

    def addCity(self,city):
        self.destinationCities.append(city)

    def getCity(self,index):
        return self.destinationCities[index]

    def numberOfCities(self):
        return len(self.destinationCities)







