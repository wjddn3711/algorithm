'''
N 개의 랜선을 만들어야 합니다
- 이미 K개의 랜선이 있습니다
- K개의 랜선의 길이는 제각각입니다
- 모두 N개의 같은 길이의 랜선으로 만들어야 하기에 K개의 랜선을 잘라서 만듭니다
- 자르고 남은 자투리는 버립니다
- N 개보다 많이 만드는 경우도 괜찮지만 최대 길이가 되려면 N개에 맞추는것이 좋아보입니다

'''
n,k = map(int,input().split())
cables = list(int(input()) for _ in range(n)) # n 개의 케이블의 길이를 저장

# 입력값의 범위가 크기에 n제곱보다는 작게 시간복잡도를 구상합니다
# 가장 작은것을 기준으로 이분탐색하여 계산해봅니다

'''
naive 하게 풀었을 경우
cable.sort()
for cut in range(cable[0],0,-1):
    lan = 0
    for c in cable:
        lan+= c//cut
    if lan >= k:
        print(cut)
        break

'''

# 이분 탐색을 썼을때
start, end = 1, max(cables) # 이분탐색 처음과 끝위치
while start<= end:
    mid = (start+end)//2 # 중간위치
    lan = 0 # 랜선 수
    for cable in cables:
        lan+= cable//mid # 각 케이블을 mid 로 쪼개었을 때에 나오는 선의 개수
    if lan >= k: # k 개 이상을 만들 수 있다면 시작점을 한칸 앞으로 땡긴다
        start = mid +1
    else:
        end = mid-1

