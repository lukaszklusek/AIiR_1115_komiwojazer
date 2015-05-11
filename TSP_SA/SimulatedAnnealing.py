#!/usr/bin/env python
__author__ = 'Wiktor&LukaszK'
import sys
import os.path
import sqlite3

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from TSP_SA.City import City
from TSP_SA.TourManager import TourManager
from TSP_SA.Tour import Tour

import math
import random
import numpy

#from ..Server.app.models import Task
#from flask import requests

from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE

path = '/home/lukas/Documents/PycharmProjects/AIiR_1115_komiwojazer/AIiR_1115_komiwojazer/Server/app.db'
connect = sqlite3.connect(path)
connect.isolation_level = None

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
c = connect.cursor()


class SimulatedAnnealing(object):


    def acceptanceProbability(self,energy,newEnergy,temperature):
        if newEnergy < energy:
            return 1.0
        return math.exp((energy-newEnergy)/temperature)

    def algorithm(self):
        tourManager = TourManager()
        tourManager2 = TourManager()
        tourManager3 = TourManager()

        f = open('test.txt','r')
        for line in f:
            a=line.split()
            ab = int(a[0])
            abc = int(a[1])
            city = City(ab, abc)
            tourManager.addCity(city);

        f.close()

        temp = 1000
        coolingRate = 0.002

        currentSolution = Tour(tourManager)
        currentSolution.generateIndividual()

        print(currentSolution)
        start=currentSolution
        print("Initial solution distance: " + str(currentSolution.getDistance()))
        poczatek = str(currentSolution.getDistance())

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
            koniec = best.getDistance()
            temp *= 1-coolingRate

        connect.execute('INSERT INTO task (input, output, time_started, user_id) VALUES (?, ?, current_timestamp, 1)',(poczatek, koniec))

        return best.getDistance()

sb = numpy.zeros(1)
sa = SimulatedAnnealing()

sb[0]=sa.algorithm()

print sb, "Najlepszy wedlug ", rank

recv_buffer = numpy.zeros(1)

if rank == 0:
        so_best = sb[0]
        for i in range(1, size):
                comm.Recv(recv_buffer, ANY_SOURCE)
                if (so_best>recv_buffer):
                    so_best = recv_buffer[0]
               # print ("Final solution distance the best: ", so_best)
else:
        # all other process send their result
        comm.Send(sb)

if comm.rank == 0:
    print "Final solution distance the best: ", so_best


connect.close()



