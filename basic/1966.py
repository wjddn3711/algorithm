t=int(input())
for i in range(t):
    cnt = 0
    n, m = map(int,input().split())
    temp = list(map(int, input().split()))
    imp = []
    for j in range(len(temp)):
        imp.append([j,temp[j]])
    found = False
    count = 0
    while True:
        if imp[0][0] == max(imp, key=lambda x:x[1])[1]:
            count+=1
            if imp[0][1] ==m :
                print(count)
                break
            else:
                imp.pop(0)
        else:
            imp.append(imp.pop(0))



