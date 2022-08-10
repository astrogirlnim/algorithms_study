#25
def digitFib(n):
    """
    Finds the first fibonacci term with n digits.
    """
    fib = [1,1,2]

    i  = 2
    while len(str(fib[-1])) < n:
        fib.append(fib[i] + fib[i-1])
        i += 1

    print(len(fib))

num = int(input())
digitFib(num)