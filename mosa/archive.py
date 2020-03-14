import solution
from objective import Objective as Objective
import copy
import random

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
        '''compares the two solutions, based on all the objectives provided
        returns: winning solution, Dom_ave, Dom_abs
        Dom_ave is for adjusting acceptance probability
        Dom_abs is for clustering'''
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
        
        return s_win, Dom_total/len(self.Objective_set.keys()), Dom_s1-Dom_s2


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
        self.make_solution_xtable()
        clusters = [[s] for s in self.Solution_set]
        while len(clusters)>final_size:
            min_diff = 99999
            merge_i = 0
            merge_ii = 1
            for c_i in range(len(clusters)):
                for c_ii in range(c_i+1, len(clusters)):
                    sum_diff = 0
                    for s1 in clusters[c_i]:
                        for s2 in clusters[c_ii]:
                            sum_diff += self.solution_xtable[str(s1.id)][str(s2.id)]
                    sum_diff = sum_diff / (len(clusters[c_i])*len(clusters[c_ii]))
                    if sum_diff < min_diff:
                        merge_i = c_i
                        merge_ii = c_ii
                        min_diff = sum_diff
            clusters[merge_i] += clusters[merge_ii]
            del clusters[merge_ii]
        self.Solution_set = []
        for c in clusters:
            self.Solution_set += c[random.randint(0,len(c))]
    
    def make_solution_xtable(self):
        '''update the table that stores how each solution perform
            in relation to each other'''
            #can be made faster 2 times faster
        self.solution_xtable = {}
        for solution1 in self.Solution_set:
            xrow = {}
            self.solution_xtable[str(solution1.id)] = xrow
            for solution2 in self.Solution_set:
                if solution1.id != solution2.id:
                    _ , _ ,xrow[str(solution2.id)] = self.Objective_compare(solution1, solution2)
        

    def Optimize(self):
        while self.temperature >= self.min_temperature:
            #run optimization algorithm here
