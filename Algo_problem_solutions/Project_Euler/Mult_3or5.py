def mult3or5(n):
    """
    Finds the sum of the multiples of 3 or 5 below the number n.
    """
    mult3 = 1
    mult5 = 1

    num_checked = []

    while mult3*3 < n:
        num_checked.append(mult3*3)
        mult3 += 1
    
    while mult5*5 < n:
        if mult5*5 not in num_checked:
            num_checked.append(mult5*5)
        mult5 += 1
    
    return sum(num_checked)

num = input()
num = int(num)
print(mult3or5(num))