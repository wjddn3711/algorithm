'''
불만도 = |A-B|
불만도가 최소가 되도록
'''

n = int(input())
rank = []
for _ in range(n):
    rank.append(int(input()))
rank.sort() # 가등수를 우선 오름차순으로 정렬

result = 0
for i in range(n):
    result += abs((i+1)-rank[i])

print(result)