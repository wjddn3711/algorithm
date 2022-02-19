n = int(input())
vector = [list(map(int,input().split())) for _ in range(n)]
vector.sort(key=lambda x:(x[0],x[1]))
[print(x,y) for x,y in vector]