

def factorize(n):
    """
    Returns prime factors of a number.
    """
    factors = []
    primes = [2]
    start = 2

    while start <= n:
        if n % start == 0:
            factors.append(start)
            n /= start
        else:
            # get the next prime
            start += 1
            while start <= n:
                is_prime = True
                for i in primes:
                    if start % i == 0:
                        is_prime = False
                
                if is_prime:
                    primes.append(start)
                    break
                else:
                    start += 1
    
    return factors

def smallest_multiple(n):
    """
    Provides the smallest number that is evenly divisible from 1 to n.
    """
    total_f = {}

    for j in range(1, n + 1):
        f = factorize(j)
        f_set = set(f)

     
        for fs in f_set:
            c = f.count(fs)
            if fs not in total_f:
                total_f[fs] = c
            else:
                if total_f[fs] < c:
                    total_f[fs] = c
    
    mult = 1
    for j in total_f.keys():
        mult *= j**(total_f[j])
    
    return mult

num = int(input())
print(smallest_multiple(num))