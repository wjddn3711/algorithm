dataStack= []
def push(data):
    dataStack.append(data)

def pop():
    pData = dataStack[-1]
    del dataStack[-1]
    return pData

for i in range(10):
    push(i)

print(pop())
