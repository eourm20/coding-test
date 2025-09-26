import sys
input = sys.stdin.readline

C = int(input())
N = int(input())

graph = [[] for _ in range(C+1)]
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append((b))
    graph[b].append((a))
    
stack = [(1)]
bias = 0
visited = [False] * (C+1)

while stack:
    n = stack.pop()
    visited[n] = True
    for nn in graph[n]:
        if visited[nn] == False:
            visited[nn] = True
            bias+=1
            stack.append((nn))
print(bias)
