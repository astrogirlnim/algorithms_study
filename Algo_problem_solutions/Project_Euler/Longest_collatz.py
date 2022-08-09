# 14
def longestCollatz(n):
    """
    Gives the longest collatz chain from starting numbers up to n.
    """
    collatz = {1:0}
    max_chain = 0
    max_start = 1
    for i in range(1,n+1):
        dist = 0
        c = i
        while c not in collatz:
            if c % 2 == 0:
                c /= 2
            else:
                c = 3*c + 1
            
            dist += 1
        
        collatz[i] = collatz[c] + dist
        if collatz[i] > max_chain:
            max_chain = collatz[i]
            max_start = i
    
    return max_start
            
print(longestCollatz(999999))