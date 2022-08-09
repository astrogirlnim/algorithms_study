# 11
def maxGridProd(g, k):
    """
    Get the greatest products of 4 adjacent numbers in grid g.
    G is assumed to be a square grid of side n >= 4.
    Numbers must be adjacent in same direction (up, down, left, right, diagonally).
    """
    max_prod = 0

    # horizontal
    l = len(g)
    max_prod = 0

    # horizontal
    for i in range(l):
        for j in range(l-3):
            p = 1
            for n in range(k):
                p *= g[i][j+n]
            
            max_prod = max(max_prod, p)
    
    # vertical
    for i in range(l):
        for j in range(l-3):
            p = 1
            for n in range(k):
                p *= g[j + n][i]
            
            max_prod = max(max_prod, p)
    
    # diagonal positive
    for i in range(l-3):
        for j in range(l-3):
            p = 1
            for n in range(k):
                p *= g[i+n][j+n]
            
            max_prod = max(max_prod, p)
    
    # diagonal negative
    for i in range(l-3):
        for j in range(3,l):
            p = 1
            for n in range(k):
                p *= g[j-n][i+n]
            max_prod = max(max_prod, p)

    return max_prod
    


        
    

g = []
# hard-coded path for now
with open("algorithms_study\\Algo_problem_solutions\\Project_Euler\\inputs\\2020grid.txt", 'r') as gf:
    for line in gf:
        mat_line = line
        if '\n' in mat_line:
            i = mat_line.index('\n')
            mat_line = mat_line[:i]
        mat_line = mat_line.split(' ')

        mat_line = [int(x) for x in mat_line]

        g.append(mat_line)

print(maxGridProd(g, 4))