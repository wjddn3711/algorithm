N,M = map(int,input().split())
numList = list(map(int,input().split()))

prob = []
for i in range(len(numList)):
    for j in range(i+1, len(numList)):
        for k in range(j+1,len(numList)):
            p =numList[i]+numList[j]+numList[k]
            if p<=M:
                prob.append(p)
print(max(prob))
