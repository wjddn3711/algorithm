
'''
-C 개의 문자들이 주어졌을 떄, L길이의 암호를 모두 찾아야함
-따라서 C개의 문자들 중에서 L개를 선택하는 모든 조합을 고려합니다
 - 조합 라이브러리를 사용하면 해결가능
 - DFS를 이용하여 조합 함수를 구현할 수 있습니다
'''
import copy
from itertools import combinations

combinations

string = []
visited = []
result = []

# 조합 함수 구현
def combination(arr, length, index):
    # 길이가 length인 모든 조합 찾기
    if len(string) == length:
        result.append(copy.deepcopy(string))
        return
    # 각 원소를 한 번씩만 뽑도록 구성
    for i in range(index, len(arr)):
        if i in visited:
            continue # 해당 인덱스의 번호를 방문했다면 무시
        string.append(arr[i]) # 문자열에 i 번째 문자를 추가
        visited.append(i) # i 번째를 방문처리
        combination(arr,length,i+1) # 만약 i 로 시작하는 l 개의 문자열을 모두 구했다면 다음으로
        string.pop()
        visited.pop()



l,c = map(int,input().split())
alphaList = list(input().split())
vowel = ['a','e','i','o','u'] # 모음 모음

alphaList.sort() # 정렬된 문자열만 가능

combination(alphaList,l,0)
for combo in result:
    vCnt = 0
    for c in combo:
        if c in vowel:
            vCnt+=1
    if vCnt >=1 and vCnt<=l-2:
        print(''.join(combo))
