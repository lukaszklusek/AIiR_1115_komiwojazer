__author__ = 'Wiktor'

class Path(object):
    def __init__(self,numCities):
        self.length = 0
        self.visited = 1
        self.city = []
        for i in range(0,numCities):
            self.city.append(i)

    def set(self,len,city,visited):
        self.length = len
        self.city = city
        self.visited = visited


    def __str__(self):
        output = "Visited towns: \n"
        for i in range(0,self.visited):
            output += " {0}\n".format(self.city[i])
        output += "; length = {0}\n".format(self.length)
        return output

path = Path(10)



print(path)
