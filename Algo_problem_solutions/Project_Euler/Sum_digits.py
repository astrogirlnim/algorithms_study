def sumDigits(n):
    """
    Sum of digits of 2^n.
    """
    num = 2**n
    num = str(num)
    num = [int(i) for i in num]
    return sum(num)

print(sumDigits(1000))