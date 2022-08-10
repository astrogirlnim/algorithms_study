#23
def sumDivisors(n):
    """
    Calculates the sum of the proper divisors of n.
    """
    # get divisors
    divisors = []

    for i in range(1,n):
        if i not in divisors:
            if n % i == 0:
                divisors.append(i)
            if n / i < n and n % i == 0:
                divisors.append(n/i)
    
    divisors = set(divisors)
                
    return(int(sum(divisors)))

def findAbundants():
    """
    Finds all abundant numbers between 24 and 28123.
    """
    abundants = []

    for i in range(1,28124):
        if sumDivisors(i) > i:
            abundants.append(i)

    return abundants

def getSums():
    a = findAbundants()

    sums = [1]*28124
    for x in range(0,len(a)):
        for y in range(x,len(a)):
            s = a[x] + a[y]
            if s <= 28123:
                if sums[s] == 1:
                    sums[s] = 0

    total = 0
    for x in range (1,len(sums)):
        if (sums[x] == 1):
            total +=x

    print(total)


print(getSums())
