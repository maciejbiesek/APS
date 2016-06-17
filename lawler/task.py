import numpy

class Task:
    
    def __init__(self, index, time, function):
        self.index = index
        self.time = time
        self.function = function
        self.successors = []
    
    def set_succ(self, x):
        self.successors.append(x)
        
    def rem_succ(self, x):
        if x in self.successors:
            self.successors.remove(x)
    
    def get_value(self, x):
        return numpy.polyval(self.function, x)
    
    def __str__(self):
        return str(self.index) + " " + str(self.time) + " " + str(self.function) + " " + str(self.successors)