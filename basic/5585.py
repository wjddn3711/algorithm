'''
타로는 자주 JOI잡화점에서 물건을 산다.
JOI잡화점에는 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고,
 언제나 거스름돈 개수가 가장 적게 잔돈을 준다.
타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때,
받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.

그리디 알고리즘: 매순간 최적의 경우로 계산합니다
- 거스름돈의 최소 개수를 계산
- 단순히 큰화폐단위 순서대로 잔돈을 거슬러주면 최적의 해를 얻을 수 있습니다
'''

n = int(input())
n = 1000-n
cnt = 0
while n!= 0: # 타겟이 0이 될때까지 계속합니다
    for change in (500,100,50,10,5,1):
        if n >= change:
            cnt += n//change
            n %= change
            break

print(cnt)