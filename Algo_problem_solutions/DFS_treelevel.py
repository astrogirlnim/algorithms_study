class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    # DFS with output traversal
    Q = [root]
    root.e = True # mark as explored
    v = root
    def recurOrder(v, ord):
        if v is not None:
            if ord == []:
                ord = [v.info]
            else:
                if v.info not in ord:
                    ord.append(v.info)

            if v.right is None and v.left is not None:
                return recurOrder(v.left, ord)
            elif v.right is not None and v.left is None:
                return recurOrder(v.right, ord)
            elif v.right is not None and v.left is not None:
                ord.append(v.left.info)
                ord.append(v.right.info)
                ord = recurOrder(v.left, ord)
                return recurOrder(v.right, ord)
            else:
                return ord
        
    ordering = recurOrder(v, [])

    print(ordering)
    res = ''
    for o in ordering:
        res += str(o) + ' '

    res = res[:-1]
    print(res)
        


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)