#28

num = int(input())

# Begin spiral count
sum = 1

# left corners
n = 1
degree = 0
while n < num**2:
    if n == (degree + 1)**2 or degree == 0:
        degree += 2

    n += degree
    sum += n

print(sum)