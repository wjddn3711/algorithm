priorities = [2, 1, 3, 2]
location = 2

answer = 0
# 문서의 location 을 튜플 형태로 같이 저장할 경우 해결 가능하다
printer = [(priorities[i],i) for i in range(len(priorities))]
while printer: # 프린터가 존재하는 동안 계속 반복
    maxVal = max(printer)[0] # 0 번째 인덱스끼리 비교하여 max값을 받아온다
    current = printer.pop(0) # 0번째 인덱스를 뽑아온다
    if current[0] != maxVal: # 현재 값이 최대값이 아닐경우 프린터의 마지막으로 순서를 옮긴다
        printer.append(current)
    else:
        answer +=1
        if current[1] == location:
            # 만약 현재 값이 최대값이며 처리해야할 순서라면 break
            break
print(answer)