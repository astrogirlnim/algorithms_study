#31
vals = [1,2,5,10,20,50,100, 200]
ways = [0]*(200+1)
ways[0] = 1
for i in range(len(vals)):
    for j in range(vals[i],201):
        ways[j] += ways[j - vals[i]]

print(ways)
print(max(ways))