import random
ar = random.sample(range(100),30) # 샘플 데이터 생성

def insertionSort(ar):
    for i in range(len(ar)-1):
        for j in range(i+1, 0, -1):
            if ar[j] < ar[j-1]:
                ar[j],ar[j-1] = ar[j-1],ar[j]
            else:
                break
    return ar
print(insertionSort(ar))