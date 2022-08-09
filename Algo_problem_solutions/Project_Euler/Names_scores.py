#22
def sortNames(names, alph):
    """
    Sorts the names in an array.
    """
    names.sort(key = lambda x: [alph.index(i) for i in x])
    return names

def namesScores(n, alph):
    """
    Returns the value of a name multiplied by its position in a sorted list of names.
    """
    names = sortNames(n, alph)
    sumsc = 0

    for i in names:
        ind = names.index(i)
        ind += 1

        score = 0
        for j in i:
            score += alph.index(j) + 1
        
        sumsc += ind*score

    print(sumsc)



# hard-coded path for now
with open("algorithms_study\\Algo_problem_solutions\\Project_Euler\\inputs\\p022_names.txt", 'r') as f:
    for line in f:
        n = line
        if '\n' in n:
            i = n.index('\n')
            n = n[:i]
        n = n.split('","')

        n[0] = n[0][1:]
        n[-1] = n[-1][:-1]

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = namesScores(n, alph)