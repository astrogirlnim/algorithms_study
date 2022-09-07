#33
import fractions

# First, create all 2 digit numbers
nums = []
for i in range(1,10):
    p = i * 10
    nums.extend([p + j for j in range(1,10)])

combs = 1

for n in nums:
    r = len(nums) - 1
    n2 = nums[r]

    while n < n2:
        common_digit = set(str(n)).intersection(set(str(n2)))

        if common_digit:

            for c in common_digit:
                reduced_n = [x for x in str(n)]
                reduced_n.remove(c)
                reduced_n2 = [x for x in str(n2)]
                reduced_n2.remove(c)
                reduced_n = int("".join(reduced_n))
                reduced_n2 = int("".join(reduced_n2))

                if n/n2 == reduced_n/reduced_n2:
                    combs *= reduced_n/reduced_n2

        r -= 1
        n2 = nums[r]

print(fractions.Fraction(combs).limit_denominator())
