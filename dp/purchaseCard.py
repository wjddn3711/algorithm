n = int(input())
card = list(map(int, input().split())) # 카드 값 입력받기

def dp(ar):
    d = [0] * (n+1)
    d[1]= ar[0]
    d[2]= max(ar[0]*2, ar[1])
    for i in range(3,n+1):
        d[i] = ar[i-1]
        for j in range(1, i//2+1):
            d[i] = max(d[i],d[i-j]+d[j])
    return d[-1]

print(dp(card))
