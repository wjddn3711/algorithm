# 브루트포스 형

def cal(n, p):
    result = 0
    while n >0:
        result += (n%10)**p # n 나머지의 제곱을 곱해준다
        n //= 10
    return result

def solution(start, p):
    D = [start]
    while True:
        next = cal(D[-1],p)
        if next in D:
            return D.index(next)
        else:
            D.append(next)

start, p = map(int,input().split())
# print(solution(start,p))


def bfs(start,p):
    visited = []
    needVisit = [start]
    cnt = 0
    while needVisit:
        node = needVisit.pop()
        if node not in visited:
            visited.append(node)
            needVisit.append(cal(node,p))
            cnt+=1
        else:
            return visited.index(node)

print(bfs(start,p))
