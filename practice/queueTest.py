import queue
queueList = []

def enqueue(data):
    queueList.append(data)

def dequeue():
    queueList.remove(queueList[0])

for index in range(10):
    enqueue(1)

print(queueList)
dequeue()
print(queueList)