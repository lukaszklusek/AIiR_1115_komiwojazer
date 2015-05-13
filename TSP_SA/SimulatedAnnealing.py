# -*- coding: utf-8 -*-

#!/usr/bin/env python
__author__ = 'Wiktor&LukaszK&LukaszW'
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
import time

#from ..Server.app.models import Task
#from flask import requests

from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE

path = '../Server/app.db'
connect = sqlite3.connect(path)
connect.isolation_level = None

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
c = connect.cursor()

if size<2:
    print "Za mało procesów"
    exit(1)

class SimulatedAnnealing(object):


    def acceptanceProbability(self,energy,newEnergy,temperature):
        if newEnergy < energy:
            return 1.0
        return math.exp((energy-newEnergy)/temperature)

    def algorithm(self, file):
        tourManager = TourManager()
        tourManager2 = TourManager()
        tourManager3 = TourManager()

        f = open(file,'r')
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

        #connect.execute('INSERT INTO task (input, output, time_started, user_id) VALUES (?, ?, current_timestamp, 1)',(poczatek, koniec))

        return best.getDistance()



if rank == 0:
    #while(1):
        #c.execute("""select id,... from task where state='waiting' order by time_started;""")
        #task = c.fetchone()
        #if task:
            #task_id = task[0]
            #file = task[ileśtam]

            #connect.execute('UPDATE task SET state='in progress', progress=0 WHERE id=?', (task_id))

            file = 'test.txt'
            for i in range(1, size):
                comm.Send(file, dest=i)

            recv_buffer = numpy.zeros(1)
            so_best = 99999999999
            for i in range(1, size):
                comm.Recv(recv_buffer, ANY_SOURCE)
                if (so_best>recv_buffer):
                    so_best = recv_buffer[0]
                progress = 100/size*i
                #connect.execute('UPDATE task SET progress=? WHERE id=?', (progress, task_id))
        #else:
            #time.sleep(1)

else:
        #while(1):
            # all other process send their result
            filename = numpy.zeros(1)
            comm.Recv(filename, source=0)
            sb = numpy.zeros(1)
            sa = SimulatedAnnealing()
            sb[0]=sa.algorithm(filename)
            comm.Send(sb, dest=0)
            print sb, "Najlepszy wedlug ", rank

if comm.rank == 0:
    print "Final solution distance the best: ", so_best


connect.close()



