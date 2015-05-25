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
from array import array

import math
import random
import numpy
import time

#from ..Server.app.models import Task
#from flask import requests

from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE

path = '/home/lukas/Documents/AIiR_1115_komiwojazer/Server/app.db'
connect = sqlite3.connect(path)
connect.isolation_level = None

a=0
b=1

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
c = connect.cursor()

if size<2:
    print "Za mało procesów"
    exit(1)

progress_precent = 0

class SimulatedAnnealing(object):


    def acceptanceProbability(self,energy,newEnergy,temperature):
        if newEnergy < energy:
            return 1.0
        return math.exp((energy-newEnergy)/temperature)

    def algorithm(self):
        tourManager = TourManager()

        for j in range(1,point[0]+1):
            c.execute("SELECT x FROM point_in WHERE task_id = ? AND number = ?", (task_id[0], j))
            ab = c.fetchone()
            c.execute("SELECT y FROM point_in WHERE task_id = ? AND number = ?", (task_id[0], j))
            abc = c.fetchone()
            city = City(ab[0], abc[0])
            tourManager.addCity(city);

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

            temp *= 1-coolingRate

        wynik_trasy_array = [str(best)]
        global wsp_city
        wsp_city = ((((((str(wynik_trasy_array[:]).replace("'","")).replace("[","")).replace("]","")).replace("(","")).replace(")","")).replace(",","|")).split('|')
        return best.getDistance()


state = ('working',)
c.execute("SELECT MIN(id) FROM task WHERE state = ?", state)
task_id = c.fetchone()
c.execute("SELECT points FROM task WHERE id = ?", task_id)
point = c.fetchone()

sb = numpy.zeros(1)
sa = SimulatedAnnealing()

sb[0]=sa.algorithm()

print sb, "Najlepszy wedlug ", rank

recv_buffer = numpy.zeros(1)

if rank == 0:
        so_best = sb[0]
        for i in range(1, size):
                comm.Recv(recv_buffer, ANY_SOURCE)
                progress_precent=math.fabs(progress_precent + 100/size)
                print progress_precent
                c.execute("UPDATE task SET progress = ?, state= 'progress' WHERE id = ?", (progress_precent,task_id[0]))
                if (so_best>recv_buffer):
                    so_best = recv_buffer[0]
else:
        # all other process send their result
        print "Wysyła proces: ", rank
        comm.Send(sb)


if comm.rank == 0:
    print "Final solution distance the best: ", so_best
    wynik = map(int, wsp_city)
    for y in range (1,point[0]+1):
        print wynik[a], ", ", wynik[b]
        c.execute("INSERT INTO point_out (number,x,y,taks_id) VALUES (?, ?, ?, ?)", (y,wynik[a],wynik[b],task_id[0]))
        a=a+2
        b=b+2

    c.execute("UPDATE task SET state= 'done', time_finished = (STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')), progress = 100 WHERE id = ?", task_id)


connect.close()
