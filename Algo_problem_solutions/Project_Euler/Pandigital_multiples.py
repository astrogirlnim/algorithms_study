#38

# Candidates
import itertools

pandigitals = list(itertools.permutations(range(1,10),9))
pandigitals = [int(''.join([str(y) for y in x])) for x in pandigitals]

def concat(a,b):
    x = b
    while x > 1:
        a *= 10
        x /= 10
    
    return a + b

max_n = 0
for n in range(9234, 9487):
    res = concat(n, 2*n)
    print(res)
    if res in pandigitals:
        max_n = max(max_n, res)

print("maximum multiple =", max_n)
