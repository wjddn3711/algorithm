n = int(input())
trophy = [int(input()) for _ in range(n)]
rcnt = 1
lcnt = 1
lmax = trophy[0]
for i in range(0,n):
    if trophy[i] > lmax:
        lmax = trophy[i]
        lcnt+=1
rmax = trophy[-1]
for i in range(n-2,-1,-1):
    if trophy[i] > rmax:
        rmax = trophy[i]
        rcnt+=1

print(lcnt)
print(rcnt)
