#32
import itertools

# Pandigital numbers can have at most 9 digits
p = []
for i in range(10):
    p.extend(list(itertools.permutations(range(1,10), i)))

# convert combinations to numbers
pd = []
for i in p:
    num = ''
    for x in i:
        num += str(x)

    if num != '':
        num = int(num)
        pd.append(num)

# get the multiplication
sump = 0
for i in pd:
    for j in pd:
        prod = i*j
        pstr = str(prod)
        if len(pstr) <= 9:
            ps = set([str(x) for x in pstr])
            if len(ps) == len(pstr):
                sump += prod

print(sump)
