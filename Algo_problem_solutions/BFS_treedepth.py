
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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:7
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.r7ight = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    # FIFO Queue for BFS
    root.l = 0 # level of the root
    maxl = 0 # max depth
    Q = [root]
    while len(Q) >= 1:
        v = Q.pop(0)
        currl = v.l
        if v.left is not None:
            v.left.l = currl + 1
            Q.append(v.left)
        if v.right is not None:
            v.right.l = currl + 1
            Q.append(v.right)

        if v.left is not None and v.right is not None:
            maxl = max(maxl, v.left.l, v.right.l)
        elif v.left is not None:
            maxl = max(maxl, v.left.l)
        elif v.right is not None:
            maxl = max(maxl, v.right.l)
        
    return maxl 
            


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
