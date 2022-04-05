truck_weights = [7,4,5,6]
bridge_length = 2
weight = 10

answer = 0
bridge = [0 for _ in range(bridge_length)] # 다리를 대기열 큐 처럼 사용
while bridge: # 건너야할 트럭이 존재하는 동안
    print(bridge)
    answer +=1 # 시간 경과
    bridge.pop(0)
    if truck_weights:
        if sum(bridge) + truck_weights[0] <= weight:
            # 만약 무게를 초과하지 않고 다리에 현재 트럭이 지나갈 수 있다면
            bridge.append(truck_weights.pop(0)) # 다리에 트럭을 배치
        else:
            bridge.append(0) # 해당 순번의 트럭이 지날 수 없다면 0을 넣어준다

print(answer)