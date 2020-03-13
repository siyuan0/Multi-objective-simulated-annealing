import copy
import mosa.config as config
class Solution:
    '''serves as basic class for solution'''
    def __init__(self):
        self.x = 0
        self.id = config.SOLUTION_ID
        config.SOLUTION_ID += 1
    
    def randomize(self):
        '''puts the Solution into a random state'''
        pass
    # def __str__(self):
    #     return str(self.x)

