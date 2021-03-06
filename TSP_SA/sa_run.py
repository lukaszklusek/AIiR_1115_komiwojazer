import os
import sqlite3
import time
import subprocess

path = '/home/lukas/Documents/PycharmProjects/NOWY/AIiR_1115_komiwojazer/Server/app.db'
connect = sqlite3.connect(path)
connect.isolation_level = None
c = connect.cursor()


while(1):
    try:
        state = ('ready',)
        c.execute("SELECT MIN(id) FROM task WHERE state = ? AND max_x_value is not null", state)
        result=c.fetchone()
        cmd = "mpiexec -n 2 python SimulatedAnnealing.py".split()
        #Powinno zadzialac jak w hosts damy ip virtualki lub stacji
        #U mnie chyba dzialalo
        cmd_2 = "mpiexec -hostfile hosts -n 4 python SimulatedAnnealing.py".split()

        if result[0] is not None:
            subprocess.call(cmd_2 + [str(result[0])])
            #os.system("mpiexec -n 4 python SimulatedAnnealing.py")
        else:
            print ("Czekam")
            time.sleep(5)
    except:
        print ("Baza jest uzywana! Probuje jeszcze raz")
        time.sleep(20)