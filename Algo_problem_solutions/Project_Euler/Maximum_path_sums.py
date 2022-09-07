#18

# Read input triangle
import collections


g = []
# hard-coded path for now
with open("algorithms_study\\Algo_problem_solutions\\Project_Euler\\inputs\\triangle_18.txt", 'r') as gf:
    for line in gf:
        mat_line = line
        if '\n' in mat_line:
            i = mat_line.index('\n')
            mat_line = mat_line[:i]
        mat_line = mat_line.split(' ')

        mat_line = [int(x) for x in mat_line]

        g.append(mat_line)

hash = {}
def maxSum(depth, index):
    if depth == len(g) - 1:
        return g[depth][index]

    if tuple([depth, index]) in hash:
        return hash[tuple([depth, index])]

    res = g[depth][index] + max(maxSum(depth+1, index),maxSum(depth +1, index+1))
    hash[tuple([depth, index])] = res

    return res

print(maxSum(0,0))    

