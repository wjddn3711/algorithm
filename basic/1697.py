from collections import deque

'''
수빈이는 동생과 숨바꼭질을 하고 있다.
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
'''


'''
특정 위치까지 이동하는 최단 시간을 계산하는 문제
이동시간이 모두 1초로 동일하므로, 간단히 BFS를 이용하여 해결가능
큐 구현을 위해 deque를 사용
'''
n,k = map(int, input().split())

visited = [0]*100001

def bfs(v):
    q = deque([v])
    while q:
        node = q.popleft()
        if node==k:
            return visited[node]
        for next in (node-1, node+1, node*2):
            if 0<= next < 100001 and not visited[next]:
                visited[next] = visited[node]+1
                q.append(next)

print(bfs(n))