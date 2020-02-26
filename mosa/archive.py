from solution import Solution as Solution
from objective import Objective as Objective

class Archive:
    def __init__(self, max_iter=10000, size_upper=15, size_lower=5):
        self.temperature = 1 # begins annealling schedule at temperature = 1
        self.min_temperature = 1/max_iter # minimum temperature the algorithm will work at
        self.coolrate = max_iter ** (-1/max_iter) # sets the coolrate to achieve max_iter number of cycles

    def reset(self):
        self.Solution_set = []
        self.temperature = 1

    def __str__(self):
        return self.Solution_set, self.temperature

    def Optimize(self):
