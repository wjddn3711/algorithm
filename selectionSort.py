import random
ar = random.sample(range(30), 20)

def selectSort(data):
    for i in range(len(data)-1):
        lowest = i
        for j in range(i+1, len(data)):
            if data[lowest] > data[j]: # 만약 j번째가 i번째(기준) 보다 작다면 min 값 저장
                lowest = j
        data[lowest],data[i] = data[i], data[lowest] # 값의 스왑
    return data

print(selectSort(ar))