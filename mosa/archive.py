import solution
from objective import Objective as Objective
import copy

class Archive:
    def __init__(self, Solution_ref, t_cycles=500, iter_per_cycle=10, size_upper=15, size_lower=5):
        self.temperature = 1 # begins annealling schedule at temperature = 1
        self.min_temperature = 1/t_cycles # minimum temperature the algorithm will work at
        self.coolrate = t_iter ** (-1/t_cycles) # sets the coolrate to achieve max_iter number of cycles
        self.Solution_Class = Solution_ref.__class__ # the reference solution class
        self.Objective_set = {} # prepares dictionary to store objectives
        self.iter_per_cycle = iter_per_cycle # number of solutions to look for at each temperature
        self.SL = size_upper
        self.HL = size_lower
        self.reset()

    def Objective_set(self,*args):
        '''sets the objectives for the given problem.
            objectives should output a value of 0-1 given an input solution, with
            1 being complete achieving of objective, and 0 being a total miss'''
        for obj in args:
            self.Objective_set[obj.name] = obj

    def Objective_compare(self, s1, s2):
        '''compares the two solutions, based on all the objectives provided'''
        Dom_total = 0
        Dom_s1 = 0
        Dom_s2 = 0
        for o_name, o in self.Objective_set.items():
            diff = o.compare(s1,s2)
            Dom_total += diff
            if diff > 0:
                Dom_s1 += diff
            elif: diff < 0:
                Dom_s2 += diff
            else:
                pass
        if (Dom_s1 == 0 and Dom_s2 == 0) or (Dom_s1*Dom_s2 != 0):
            #for the case of non-dominating solutions
            s_win = None
        elif Dom_s1 != 0:
            # solution1 wins
            s_win = s1
        else:
            # solution2 wins
            s_win = s2
        
        return s_win, Dom_total/len(self.Objective_set.keys())


    def reset(self):
        self.Solution_set = []
        self.temperature = 1

        # fills up the archive with random solutions up to SL
        for i in range(self.SL):
            Solution_new = self.Solution_Class()
            Solution_new.randomize()
            self.Solution_set.append(Solution_new)

    def __str__(self):
        return self.Solution_set, self.temperature

    def clustering(self, final_size = 1):
        '''reduces the archive size to desired amound
            by removing solutions that are close to each other'''
        
        clusters = [[s] for s in self.Solution_set]



    def Optimize(self):
        while self.temperature >= self.min_temperature:
            #run optimization algorithm here
