#13
def largeSum(arr,k):
    """
    Computes up to k digits of the sum of all numbers in arr.
    Assumes incoming numbers are in string format and of the same length.
    """
    s = sum(arr)
    s = str(s)

    n = s[:k]
    return int(n)


    

a = []
# hard-coded path for now
with open("algorithms_study\\Algo_problem_solutions\\Project_Euler\\inputs\\largenums.txt", 'r') as f:
    for line in f:
        num = line
        if '\n' in num:
            i = num.index('\n')
            num = num[:i]
        
        num = int(num)

        a.append(num)

k = int(input())
print(largeSum(a,k))