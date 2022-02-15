def bfs(graph, start):
    visited = []
    needVisit = []

    needVisit.append(start)
    while needVisit: # 더이상 방문할 노드가 없을때 까지
        node = needVisit.pop(0) #0번째 인덱스를 빼오고 앞을 채운다 (큐와 같은 원리)
        if node not in visited:
            visited.append(node)
            needVisit.extend(graph[node]) # 노드의 나머지 데이터를 넣는다

    return visited

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(bfs(graph,'A'))

