import sys
import mosa
from mosa import solution
import random
import copy
a = mosa.Solution()

class aa:
    def __init__(self):
        self.x = 1
    def help11(self):
        print("lol")
    def rand(self):
        self.x = random.randint(1,10)
        self.help11()
        return 1,2,3
    
    def __str__(self):
        return str(self.x)

a = aa()
q1,_,_ = a.rand()
print(q1)