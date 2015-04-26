__author__ = 'Wiktor'
from TSP_MPI.City import City

class TourManager(object):
    destinationCities = []

    def addCity(self,city):
        self.destinationCities.append(city)

    def getCity(self,index):
        return self.destinationCities[index]

    def numberOfCities(self):
        return len(self.destinationCities)

    def getIndividualDistance(self,index1,index2):
        print(self.destinationCities[index1])
        return self.destinationCities[index1].distanceTo(self.destinationCities[index2])

