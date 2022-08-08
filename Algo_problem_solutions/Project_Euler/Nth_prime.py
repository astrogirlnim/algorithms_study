def nth_prime(n):
    """
    Finds the nth prime.
    """
    primes = [2]
    start = 2
    n -= 1
    while n > 0:
        # find the next prime
        np = start + 1
        is_prime = False
        while not is_prime:
            is_prime = True
            for i in primes:
                if np % i == 0:
                    is_prime = False
            
            if is_prime:
                break
            else:
                np += 1
        
        primes.append(np)
        start = np
        n -= 1
    
    return primes[-1]

num = int(input())
print(nth_prime(num))
    