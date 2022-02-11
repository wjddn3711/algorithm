import random
sample = random.sample(range(100),10)
print(sample)
def mergesplit(data):
    d = len(data)
    if d <=1:
        return data
    return merge(mergesplit(data[:d//2]), mergesplit(data[d//2:]))

def merge(left, right):
    sortedList = []
    l, r = 0,0
    while l<len(left) and r<len(right):
        if left[l] < right[r]: # left가 right 보다 작다면
            sortedList.append(left[l])
            l+=1
        else:
            sortedList.append(right[r])
            r+=1
    while l<len(left):
        sortedList.append(left[l])
        l+=1
    while r<len(right):
        sortedList.append(right[r])
        r+=1
    return sortedList

print(mergesplit(sample))