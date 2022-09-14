#36
s = 0
for n in range(1000000):
    dn = [x for x in str(n)]
    bin_n = format(n, 'b') 
    if dn == dn[::-1] and bin_n == bin_n[::-1]:
        s += n

print("Double base palindrome sum =", s)