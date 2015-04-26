__author__ = 'Wiktor'

from TSP_MPI.Tour import Tour
from TSP_MPI.City import City
from TSP_MPI.TourManager import TourManager

class MatrixTour(object):
    def __init__(self,tourManager):
        self.cities = []
        self.countOfCities = len(tourManager.destinationCities) -1
        print(self.countOfCities)
        for i in range(0,self.countOfCities):
            for j in range(0,self.countOfCities):
                self.cities[i][j] = tourManager.getIndividualDistance(i,j)



cities = []
tourManager = TourManager()
for i in range(0,10):
    tourManager.addCity(City())

matrixTour = MatrixTour(tourManager)

print(matrixTour.cities)
