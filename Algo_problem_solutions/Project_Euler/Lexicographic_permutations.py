#24
import itertools
n = list(range(10))
n = [str(x) for x in n]
c = list(itertools.permutations(n, 10))

#convert to ints
nums = []
for x in c:
    num = ''
    for j in x:
        num += j
    
    nums.append(int(num))

print(nums[1000000 - 1])

