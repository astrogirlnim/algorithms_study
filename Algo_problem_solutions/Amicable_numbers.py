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
    
    divisors.sort()
    return(int(sum(divisors)))

def amicableNumbers(n):
    anumbers = []
    checked = []
    sum_anumbers = 0
    i = 1
    greatest_num = 0
    while greatest_num < n:
        if i not in anumbers:
            a = sumDivisors(i)
            b = sumDivisors(a)

            if i == b and b != a:
                greatest_num = max(a,b,greatest_num)
                anumbers.extend([i,a]) 
        
        i += 1
    anumbers = [x for x in anumbers if x < n]
    print(sum(anumbers))
            

n = int(input())
amicableNumbers(n)