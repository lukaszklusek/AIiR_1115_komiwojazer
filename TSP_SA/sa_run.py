import os
import sqlite3
import time
import subprocess

path = '/home/lukas/Documents/AIiR_1115_komiwojazer/Server/app.db'
connect = sqlite3.connect(path)
connect.isolation_level = None
c = connect.cursor()

while(1):
    state = ('working',)
    c.execute("SELECT MIN(id) FROM task WHERE state = ?", state)
    result=c.fetchone()

    print result[0]

    if result[0] is not None:
        #subprocess.call("mpiexec", "-n", "4", "python", "SimulatedAnnealing.py ", +result)
        os.system("mpiexec -n 4 python SimulatedAnnealing.py")
    else:
        time.sleep(30)