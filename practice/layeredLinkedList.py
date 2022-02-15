class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head # 처음에는 head 가 tail 이다

    def insert(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else: # head 가 있다면
            node = self.head
            while node.next:
                node = node.next # 노드의 끝을 찾기 위해
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def addBefore(self,target, data):
        if self.head == None:
            print("해당하는 데이터가 없습니다")
        else:
            node = self.head
            while node:
                if node.next.data == target:
                    new = Node(data,node,node.next)
                    node.next = new
                    node.next.prev = new
                    return True
                else:
                    node = node.next
            return False

    def addAfter(self,target, data):
        if self.head == None:
            print("해당하는 데이터가 없습니다")
        else:
            node = self.head
            while node:
                if node.data == target:
                    new = Node(data,node,node.next)
                    node.next = new
                    node.next.prev = new
                    return True
                else:
                    node = node.next
            return False

    def searchFromHead(self,data):
        if self.head==None:
            return False
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def searchFromTail(self,data):
        if self.tail==None:
            return False
        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    def insertBefore(self,data,beforeData):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != beforeData:
                node = node.prev
                if node == None:
                    return False
                new = Node(data)
                beforeNew = node.prev
                beforeNew.next = new
                new.prev = beforeNew
                new.next = node
                return True


doubleLinked = NodeMgmt(0)
for i in range(1,10):
    doubleLinked.insert(i)
# print(doubleLinked.searchFromTail(2))
# print(doubleLinked.addBefore(2,1.5))
print(doubleLinked.addAfter(1,1.7))
doubleLinked.desc()
