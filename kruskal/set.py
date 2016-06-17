class Set:
    
    def __init__(self, x):
        self.value = x
        
    def __eq__(self, other): 
        return self.value == other.value
    
    def __ne__(self, other):
        return not self.__eq__(other)