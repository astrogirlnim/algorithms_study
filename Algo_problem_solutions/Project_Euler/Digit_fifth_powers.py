#30

totalsum = 0
for n in range(2,355000):
    sumn = 0
    o = str(n)
    o = [int(x) for x in o]
    for x in o:
        sumn += x**5

    if sumn == n:
        totalsum += sumn
    
print(totalsum)
