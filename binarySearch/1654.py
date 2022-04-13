k, n = map(int,input().split())
cables = [int(input()) for _ in range(k)] #n 개의 랜선을 입력받는다
cables.sort() #
end = cables[-1] # 가장 큰값을 end 로 둔다
start = 1

def check(x):
    cnt = 0
    for lan in cables:
        cnt+=lan//x # x 로 쪼개었을 경우 얻게되는 선의 개수를 더해준다
    return cnt

result = 0
while start<=end: # start 가 end 보다 클때까지 즉, 해당 하는 값을 찾게 될때까지 반복
    mid = (start+end)//2 # 중간값은 시작점+끝점 의 반
    cnt = check(mid)
    if cnt == n:
        result = mid
        break
    elif cnt > n: # mid 로 나눈 값이 n 보다 크다면 범위를 좁혀준다
        start = mid
    else: # n 보다 작다면 범위를 늘려준다
        end = mid

print(result)



