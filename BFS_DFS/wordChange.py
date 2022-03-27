from collections import deque

begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]

answer = 0
n = len(words)
if target not in words:
    print(0)

def check(w1,w2): # 단어 두개를 받아 두 단어가 변환 가능한지 여부를 체크
    ns = len(w1)
    cnt = 0
    for i in range(ns):
        if w1[i]!=w2[i]:
            cnt+=1
    if cnt>1:
        return False
    return True

result = []
def dfs(start, cost, visited):
    if start==target:
        result.append(cost)
        return
    for i in range(n):
        if check(start,words[i]) and words[i] not in visited:
            visited.append(words[i])
            dfs(words[i],cost+1,visited)
            visited.pop()

dfs(begin,0,[])
print(result)