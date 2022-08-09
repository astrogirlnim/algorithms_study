#20
def factorialSum(n):
    """
    Sums the digits of the factorial of n.
    """
    f = 1
    for i in range(2,n+1):
        f *= i

    f = str(f)
    s = 0
    for d in f:
        s += int(d)
    
    return s

n = int(input())
print(factorialSum(n))