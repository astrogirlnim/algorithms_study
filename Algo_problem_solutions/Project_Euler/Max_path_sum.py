#18
def maxPathSum(t):
    """
    Finds the maximum sum of a path of adjacent numbers in a triangle t.
    """

    final_sum = 0
    previ = 0
    for i in t:
        print(i)
        if len(i) == 1:
            final_sum += i[0]
        else:
            # offset i by 1
            previ += 1
            # retrieve candidates
            candidates = i[previ-1:previ+1]
            print(candidates)

            # get max of candidates
            max_c = max(candidates)
            maxi = i.index(max_c)
            previ = maxi
            print("winner=",max_c)

            final_sum+=max_c
        
    print("Total=", final_sum)


t = []
# hard-coded path for now
with open("algorithms_study\\Algo_problem_solutions\\Project_Euler\\inputs\\triangle_18.txt", 'r') as f:
    for line in f:
        mat_line = line
        if '\n' in mat_line:
            i = mat_line.index('\n')
            mat_line = mat_line[:i]
        mat_line = mat_line.split(' ')

        mat_line = [int(x) for x in mat_line]

        t.append(mat_line)

maxPathSum(t)