n = int(input())
k = 0
cnt = 0
while n!=0:
    k+=1
    if n < k:
        k=1
    n -= k
    cnt+=1
print(cnt)