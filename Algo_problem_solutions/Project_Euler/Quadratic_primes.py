def primeGenerator(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def quadPrimes():
    start = 0
    # Sample n of 1000
    n = 0
    max_primes = 0
    maxab = 0

    p = primeGenerator(1001)
    totalp = primeGenerator(87400)
    p.extend([-x for x in p])
    p.sort()

    # b has to be prime
    for a in range(-1000,1001):
        for b in p:
            # generates nums
            nc = n**2 + a*n + b
            c = 0
            while nc in totalp:
                c += 1
                n += 1
                nc = n**2 + a*n + b
            
            # reset
            n = 0

            if max_primes < c:
                max_primes = c
                maxab = a*b
    
    print(maxab)
                
quadPrimes()



