graph = {
0:  [2],
1: [2,3],
2:[0,1,3,4],
3:[1,2],
4:[2,5,6],
5:[4,6],
6:[4,5],
}
def dfs(start):
  stack = [start]
  visited = []

  while stack:
    node = stack.pop()
    if node not in visited:
      visited.append(node)
      for neighbor in graph[node]:
        stack.append(neighbor)
  return visited

print(dfs(3))