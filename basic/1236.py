n,m = map(int, input().split())
castle = []
for _ in range(n):
    s = input()
    castle.append(s)

row = [0]*n
col = [0]*m

for i in range(n):
    for j in range(m):
        if castle[i][j] =='X':
           row[i] = 1
           col[j] = 1

rowCnt = row.count(0)
colCnt = col.count(0)
print(max(rowCnt,colCnt))