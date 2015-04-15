__author__ = 'Wiktor'

from TSP_SA.City import City

class TourManager(object):
    destinationCities = []

    def addCity(self,city):
        self.destinationCities.append(city)

    def getCity(self,index):
        return self.destinationCities[index]

    def numberOfCities(self):
        return len(self.destinationCities)







