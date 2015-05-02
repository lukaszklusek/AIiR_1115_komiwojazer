#!/usr/bin/env python
__author__ = 'Wiktor&LukaszK'
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from TSP_SA.City import City
from TSP_SA.TourManager import TourManager
from TSP_SA.Tour import Tour
import math
import random
import numpy

from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

class SimulatedAnnealing(object):


    def acceptanceProbability(self,energy,newEnergy,temperature):
        if newEnergy < energy:
            return 1.0
        return math.exp((energy-newEnergy)/temperature)

    def algorithm(self):
        tourManager = TourManager()
        tourManager2 = TourManager()
        tourManager3 = TourManager()
        city = City(60, 200)
        tourManager.addCity(city);
        city2 = City(180, 200);
        tourManager.addCity(city2);
        city3 = City(80, 180);
        tourManager.addCity(city3);
        city4 = City(140, 180);
        tourManager.addCity(city4);
        city5 = City(20, 160);
        tourManager.addCity(city5);
        city6 = City(100, 160);
        tourManager.addCity(city6);
        city7 = City(200, 160);
        tourManager.addCity(city7);
        city8 = City(140, 140);
        tourManager.addCity(city8);
        city9 = City(40, 120);
        tourManager.addCity(city9);
        city10 =  City(100, 120);
        tourManager.addCity(city10);
        city11 = City(180, 100);
        tourManager.addCity(city11);
        city12 = City(60, 80);
        tourManager.addCity(city12);
        city13 =  City(120, 80);
        tourManager.addCity(city13);
        city14 =  City(180, 60);
        tourManager.addCity(city14);
        city15 =  City(20, 40);
        tourManager.addCity(city15);
        city16 =  City(100, 40);
        tourManager.addCity(city16);
        city17 = City(200, 40);
        tourManager.addCity(city17);
        city18 =  City(20, 20);
        tourManager.addCity(city18);
        city19 =  City(60, 20);
        tourManager.addCity(city19);
        city20 = City(160, 20);
        tourManager.addCity(city20);

        temp = 1000
        coolingRate = 0.002

        currentSolution = Tour(tourManager)
        currentSolution.generateIndividual()

        print(currentSolution)
        print("Initial solution distance: " + str(currentSolution.getDistance()))

        best = Tour(tourManager)
        best.generateIndividual()
        best.cpTour(currentSolution.tourManager)

        newSolution = Tour(tourManager)
        newSolution.generateIndividual()
        while (temp > 1):

            newSolution.cpTour(currentSolution.tourManager)
            tourPos1 = random.randint(0,newSolution.tourSize()-1)
            tourPos2 = random.randint(0,newSolution.tourSize()-1)

            citySwap1 = newSolution.getCity(tourPos1)
            citySwap2 = newSolution.getCity(tourPos2)

            newSolution.setCity(tourPos2, citySwap1)
            newSolution.setCity(tourPos1, citySwap2)

            currentEnergy = currentSolution.getDistance()
            neighbourEnergy = newSolution.getDistance()

            if (self.acceptanceProbability(currentEnergy,neighbourEnergy,temp) > random.random()):
                currentSolution.cpTour(newSolution.tourManager)
            if (currentSolution.getDistance() < best.getDistance()):
                best.cpTour(currentSolution.tourManager)

            #temp -= 100
            temp *= 1-coolingRate

        print("Final solution distance: " + str(best.getDistance()))
        print(best)


sa = SimulatedAnnealing()

sb=sa.algorithm()

recv_buffer = numpy.zeros(1)

if rank == 0:
        so_best = 999999
        for i in range(1, size):
                comm.Recv(recv_buffer, ANY_SOURCE)
                if (so_best<recv_buffer):
                    so_best = recv_buffer[0]
                print ("Final solution distance the best: ", so_best)
else:
        # all other process send their result
        comm.Send(sb)

if comm.rank == 0:
    print ("Final solution distance the best: ", so_best)



