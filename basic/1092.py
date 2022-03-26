'''
지민이는 항구에서 일한다. 그리고 화물을 배에 실어야 한다. 모든 화물은 박스에 안에 넣어져 있다.
항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다. 모든 크레인은 동시에 움직인다.

각 크레인은 무게 제한이 있다. 이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다.
모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성하시오.
'''

n = int(input())
crain = list(map(int,input().split()))
m = int(input())
box = list(map(int,input().split()))
box.sort(reverse=True)
crain.sort(reverse=True)

# 각 크레인이 현재 옮겨야 하는 박스의 번호 (0부터)
positions = [0]*n
# 각 박스를 옮겼는지의 여부
checked = [False]*m

cnt,result = 0,0
if max(crain) < max(box):
    print(-1) # 만약 크레인의 최대무게가 최소무게의 박스보다 작다면 -1
else:
    while True:
        if cnt == m: break # 박스를 다 옮겼다면 종료
        for i in range(n): # 모든 크레인에 대하여 각각 처리
            while positions[i] < m:
                # 아직 안 옮긴 박스 중에서 옮길 수 있는 박스를 만날때까지 반복
                if not checked[positions[i]] and crain[i] >= box[positions[i]]:
                    checked[positions[i]] = True
                    cnt +=1
                    break
                positions[i] +=1
        result+=1
    print(result)