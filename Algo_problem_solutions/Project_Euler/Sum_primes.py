def sumPrimes(n):
    """
    Sums all primes with value below n.
    """
    primes = [2]
    start = 2
    sum = 0

    while start < n:
        sum += start

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
    
    return sum

num = int(input())
print(sumPrimes(num))