# Поиск в ширину на графе
#                      0
#                    /   \
#                   /     \
#                  1       2
#                /  \     /
#              3 ---- 4 -+
#

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0', '4']),
         '3': set(['1', '4']),
         '4': set(['2', '3', '1'])
         }

# поиск в глубину
def dfs(graph, start, visited=[]):
    visited.append(start)
    for v in graph[start]:
        if v not in visited:
            visited = dfs(graph, v, visited)
        return visited

# поиск в ширину
def bfs(graph, start, visited=[]):
    queue = []
    visited.append(start)
    queue.append(start)
    while queue:
        start = queue.pop(0)
        for v in graph[start]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited



print(f"Поиск в глубину{dfs(graph, '3')}")
print(f"Поиск в ширину{bfs(graph, '3')}")

