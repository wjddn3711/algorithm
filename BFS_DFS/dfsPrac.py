def dfs(graph,start):
    visited, needVisit = [], []
    needVisit.append(start)

    while needVisit:
        node = needVisit.pop() # 스택이기 때문에 맨뒤의 데이터를 뽑아온다
        if node not in visited:
            visited.append(node)
            needVisit.extend(graph[node])
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

print(dfs(graph,'A'))

