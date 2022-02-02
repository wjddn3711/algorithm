class Node:
    def __init__(self,data, next=None):
        self.data = data
        self.next = next # 두번째 인자가 없다면 DEFAULT 인 none 이 들어감

def add(data):
    node = head
    while node.next:
        node = node.next
    # 마지막 노드가 node 가 node 가 된다
    node.next = Node(data) # 마지막 노드의 포인터에 Node 저장

def printNode(head):
    node = head
    while node.next:
        print(node.data)
        node = node.next
    print(node.data)

def searchNode(head, target):
    node = head
    search = True
    while search:
        if node.data <= target.data:
            search = False # 만약 타겟이 해당 데이터 보다 작다면 탈출
        else:
            node = node.next
    node.next, target.next = target, node.next



node1 = Node(1)
node3 = Node(1.5)
# node2 = Node(2)
# node1.next = node2
head = node1
for i in range(2,10):
    add(i)
# printNode(head)

searchNode(node1, node3)
printNode(head)