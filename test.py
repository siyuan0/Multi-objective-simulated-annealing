import sys
import mosa
from mosa import solution
import random
import copy
a = mosa.Solution()

class aa:
    def __init__(self):
        self.x = 1
    def rand(self):
        self.x = random.randint(1,10)
    def __str__(self):
        return str(self.x)

x = a.__class__
x1 = x()
print(a.id)
print(x)
print(x1.id)