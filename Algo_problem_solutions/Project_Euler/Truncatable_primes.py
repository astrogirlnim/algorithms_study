#37
def isPrime(n):
    if n in {2, 3, 5, 7}:
        return True
    if n < 2 or n%2 == 0:
        return False
    if n%3 == 0 or n%5 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0 or n%(f+2) == 0:
            return False
        f += 6
    return True

def isTrunc(x):
    x = str(x)
    for k in range(1,len(x)):
        tr_left = int(x[k:])
        tr_right = int(x[:-k])
        if not isPrime(tr_left) or not isPrime(tr_right):
            return False
    
    return True

def check(i):
    if isPrime(i):
        return isTrunc(i)

c,s,i = 0,0,11 # skip the first 4 primes
while c < 11:
    if check(i):
        c += 1
        s += i
    i += 1

print("count =", c)
print("sum =", s)
print("max prime =", i-1)