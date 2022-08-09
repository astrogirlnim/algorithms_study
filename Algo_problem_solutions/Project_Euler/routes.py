#15
def routes(n):
    """
    Calculates the number of routes, only being able to move right and down,
    from the top left to bottom right corners of an nxn grid.
    Assuming n >= 2.
    """
    total = 0
    s = {
        'val': [0,0],
        'd': None,
        'r': None,
        'e':True
    }
    def constructGraph(v, n):
        if v["val"][0] < n:
            nnode = v.copy()
            nnode["val"][0] += 1
            v['r'] = constructGraph(nnode, n)
        if v["val"][1] < n:
            nnode = v.copy()
            nnode["val"][1] += 1
            v['d'] = constructGraph(nnode, n)
        else:
            return v.copy()
    
    constructGraph(s, n)

    # every unexplored node constitutes a new path
    L = [s]
    while len(L) > 0:
        v = L.pop(0) # BFS
        v['e'] = True
        if v['d'] is not None:
            print(v['d'])
            L.append(v['d'])
            v['d']['e'] = True
            total += 1
        if v['r'] is not None:
            v['d']['e'] = True
            L.append(v['r'])
            total += 1
    
    return total



num = int(input())
print(routes(num))

