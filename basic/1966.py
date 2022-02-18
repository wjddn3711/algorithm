t=int(input())
for i in range(t):
    cnt = 0
    n, m = map(int,input().split())
    temp = list(map(int, input().split()))
    if n==1:
        print(1)
        continue
    queue = []
    for i in range(len(temp)):
        queue.append([i,temp[i]])
    cnt = 0
    while True:
        currMax = max(queue, key=lambda x:x[1])[1]
        start = queue[0]
        if start[1]==currMax:
            cnt+=1
            if start[0]==m:
                break
            queue.pop(0)
            continue
        else:
            queue.append(queue.pop(0))
    print(cnt)





