
class Node:
    def __init__(self, data, left, right):
        self.parent = -1
        self.data = data
        self.left = left
        self.right = right

def inOrder(node, level):
    global x
    if node.left != -1:
        inOrder(tree[node.left], level+1)
    maxLevel[level] = max(maxLevel[level],x)
    minLevel[level] = min(minLevel[level],x)
    x+=1
    if node.right != -1:
        inOrder(tree[node.right], level+1)


x = 1
tree = dict()
n = int(input())
maxLevel = [0]*(n+1)
minLevel = [n]*(n+1)
for i in range(1,n+1):
    tree[i] = Node(i,-1,-1)

for _ in range(n):
    data, left, right = map(int,input().split())
    tree[data] = Node(data, left,right)
    if left != -1:
        tree[left].parent = data
    if right != -1:
        tree[right].parent = data

root = 0
for i in range(1,n+1):
    if tree[i].parent == -1:
        root = i
        break

inOrder(tree[root],1)
resultLevel = 1
result = maxLevel[1]-minLevel[1]+1
for i in range(2,n+1):
    if maxLevel[i] - minLevel[i]+1 > result:
        result = maxLevel[i]-minLevel[i]+1
        resultLevel = i

print(resultLevel,result)