#12
def factorize(n):
    """
    Returns all factors of triangle numbers up to n factors.
    """
    t = 1 # latest triangle number
    nat = 2 # latest natural number
    factors = []
    while len(factors) < n:
        t += nat
        nat += 1

        factors = []
        i = 1
        # get the factors
        while i < t and i not in factors:
            if t % i == 0 and i not in factors:
                factors.extend([i, t/i])
            i += 1
        print(factors)

    
    return t 

num = int(input())
print(factorize(num))

