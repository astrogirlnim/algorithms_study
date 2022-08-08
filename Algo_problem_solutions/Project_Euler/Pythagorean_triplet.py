def pyTriplet(n):
    """
    Finds the largest Pythagorean triplet up to the number n.
    """
    # starting case
    a = 1

    for i in range(2,n-3):
        l = a
        r = n - i - a

        while l < i and i < r:
            print("a = ", l)
            print("b = ", i)
            print("c = ", r)
            if l**2 + i**2 == r**2:
                return l*i*r
            else:
                l += 1
                r -= 1
    

num = int(input())
print(pyTriplet(num))


