import random
datas = random.sample(range(100),10)
datas.sort()
print(datas)

def binary_search(data,search):
    if len(data)==1 and search == data[0]:
        return True
    if len(data)==1 and search != data[0]:
        return False
    if len(data) == 0:
        return False

    mid = len(data)//2
    if search == data[mid]:
        return True
    else:
        if search > data[mid]:
            return binary_search(data[mid:],search)
        else:
            return binary_search(data[:mid],search)


print(binary_search(datas,7))