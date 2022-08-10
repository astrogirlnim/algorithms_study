#26
def longestCycle(n):
    """
    Retrieves the digit up to n whose fraction has the longest length cycle.
    """
    max_length = 0
    max_d = 1
    for d in range(1,n):
        dec = []
        nom = 1

        while nom not in dec:
            if not nom:
                break
            
            dec.append(nom)
            nom = (nom % d) * 10

        if nom != 0:
            len_recur = len(dec) - dec.index(nom) + 1
            if len_recur > max_length:
                max_length = len_recur
                max_d = d
        
    
    print(max_length)
    print("d=",max_d)

num = int(input())
longestCycle(num)