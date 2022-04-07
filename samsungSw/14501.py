n = int(input())
plan = []

for i in range(n):
    t,p = map(int,input().split())
    plan.append([p/t, i, t, p])

plan.sort()
print(plan)
result = 0
while plan:
    curr = plan.pop(0) # 가장 효율이 좋은 일을 꺼내온다
    if curr[1]+curr[2] > n+1: # n+1 일에는 회사에 없기 때문에 불가능
        continue


