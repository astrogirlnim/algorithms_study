# 34
from xmlrpc.client import MAXINT
import math

total = 0
factorials = {}

for i in range(0,10):
    factorials[i] = math.factorial(i)

for i in range(3,2540161):
    if sum([factorials[int(x)] for x in str(i)]) == i:
        total += i

print(total)