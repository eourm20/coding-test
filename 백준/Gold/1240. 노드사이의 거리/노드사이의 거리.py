import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b, c = list(map(int, input().split()))
    graph[a].append((b, c))
    graph[b].append((a, c))
# print(graph)

def dfs(start, end):
    visited = [False] * (N+1)
    answer = 0
    stack = [(start, 0)]
    visited[start] = True
    while stack:
        node, dist = stack.pop()
        if node == end:
            answer = dist
            break
        for next_node, next_cost in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append((next_node, dist + next_cost))
    return answer
for _ in range(M):
    a, b = map(int, input().split())
    print(dfs(a, b))