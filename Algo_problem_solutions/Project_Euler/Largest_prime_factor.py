def largest_prime_factor(n):
    latest_prime = 2
    primes = [2]
    np = 2

    while n != 1:
        # find all primes up to n
        # start by dividing by the latest prime
        while n % latest_prime == 0:
            n /= latest_prime

        # check if n == 1
        if n == 1:
            return latest_prime
        else:
            # find the next prime
            np = latest_prime + 1
            while np <= n:
                is_prime = True
                for i in primes:
                    if np % i == 0:
                        is_prime = False
                
                if is_prime:
                    break
                else:
                    np += 1
            
            latest_prime = np

    


num = int(input())
print(largest_prime_factor(num))