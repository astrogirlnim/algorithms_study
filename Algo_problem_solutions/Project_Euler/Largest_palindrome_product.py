from itertools import permutations
def largestPalProduct(n):
    """
    Returns the largest palindromic product of 2 n digit numbers.
    Minimum n accepted is 1.
    """
    smallest_num = 10**(n-1)
    max_num = 9
    # calculate the max number
    while n > 1:
        max_num = max_num*10 + 9
        n -= 1
    
    nums = list(range(smallest_num, max_num + 1))
    nums.extend(nums)

    mults = list(permutations(nums, 2))
    mults = list(set(mults))
    mults.sort(reverse=True)

    palindromes = []
    
    for i in mults:
        num = i[0] * i[1]
        num = str(num)
        r = ''

        k = len(num) - 1
        while k >= 0:
            r += num[k]
            k -= 1

        is_palindrome = num == r
        
        if is_palindrome:
            palindromes.append(int(num))

    return max(palindromes)    

n = int(input())
print(largestPalProduct(n))