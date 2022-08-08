def sum_square(n):
    """
    Finds the difference between the sum of the squares and the
    square of the sum of up to n natural numbers.
    """
    square_sum = sum(range(n+1))
    square_sum **= 2

    sum_square = 0
    for i in range(1,n+1):
        sum_square += i**2
    
    return square_sum - sum_square

num = int(input())
print(sum_square(num))