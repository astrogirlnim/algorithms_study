# 32
from code import interact
import collections
import itertools

# Generate all length 1:4 pandigitals
pd = {1:list(range(1,10))}
for i in range(2,5):
    candidates = list(itertools.permutations(range(1,10),i))
    pd[i] = [int("".join([str(i) for i in x])) for x in candidates]

# Create an n x n matrix
seen = set()
cand_lengths = [(1,4),(2,3)]
res = 0

for i,j in cand_lengths:
    for x in pd[i]:
        for y in pd[j]:
            x_digits = set(str(x))
            y_digits = set(str(y))

            if not x_digits.intersection(y_digits):
                prod = x*y
                prod_digits = set(str(prod))

                if "0" not in prod_digits and len(prod_digits) == len(str(prod)): 

                    x_intersect = prod_digits.intersection(x_digits)
                    y_intersect = prod_digits.intersection(y_digits)

                    if not x_intersect and not y_intersect and prod not in seen:
                        seen.add(prod)
                        res += prod


print(res)




