class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeManager:
    def __init__(self, data):
        self.head = Node(data) #초기 데이터를 head 로

    def add(self, data):
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data)

    def printer(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self,data):
        if self.head=='':
            print("해당값을 가진 노드가 없습니다")
            return
        if self.head.data == data: # head 가 삭제될경우
            temp = self.head
            self.head = self.head.next
            del temp
        else: # 마지막, 중간 노드 삭제
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next

    def search(self,target):
        node = self.head
        while node:
            if node.data == target:
                return node
            else:
                node = node.next

linkedList1 = NodeManager(1)
for i in range(2,10):
    linkedList1.add(i)
linkedList1.printer()
print(linkedList1.search(4).data)
