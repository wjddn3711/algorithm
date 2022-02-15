from random import randint
data = []
for num in range(10):
    data.append(randint(1,100))

def seq(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

print(seq(data,72))