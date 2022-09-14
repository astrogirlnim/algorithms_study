#35
from collections import deque
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

p = deque()
p.extend(i for i in primes(1000000))

res = 0
seen = []
for x in p:
    if x not in seen:
        dx = deque([i for i in str(x)])
        rx = [x]
        for n in range(1, len(dx)):
            dx.rotate(1)
            num = int(''.join(dx))
            if num not in rx:
                rx.append(num)

        if all([j in p for j in rx]):
            print(x)
            res += len(rx)
            print("sum =", res)
        
        seen.extend(rx)


print(res)