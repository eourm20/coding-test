import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[0]*(M+1) for _ in range(N+1)]
for i in range(K):
    r, c = map(int, input().split())
    graph[r][c] = 1
# print(graph)

def dfs(i, j, graph):
    stack = []
    graph[i][j] = 0
    stack.append((i, j))
    a = 1
    while stack:
        r, c = stack.pop()
        for dr, dc in ((1,0),(-1,0),(0,1), (0, -1)):
            nr, nc = r+dr, c+dc
            # print(nr, nc)
            if 0<nr<N+1 and 0<nc<M+1 and graph[nr][nc] ==1:
                graph[nr][nc] = 0
                a+=1
                stack.append((nr, nc))
    # print(a)
    return a

answer = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if graph[i][j] == 1:
            sub_a = dfs(i, j, graph)
            if answer < sub_a:
                answer = sub_a
print(answer)
