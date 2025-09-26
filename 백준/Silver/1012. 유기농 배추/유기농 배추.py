import sys
input = sys.stdin.readline
import heapq
T = int(input())

def dfs(i, j, graph):
    stack = []
    stack.append((i, j))
    graph[i][j] = 0

    while stack:
        x, y = stack.pop()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                stack.append((nx, ny))
    
    
def testcase():
    global N, M
    answer = 0
    M, N, K = map(int, input().split())
    graph = [[0]*(M) for _ in range(N)]
    
    for _ in range(K):
        c, r = map(int, input().split())
        graph[r][c] = 1
    # print(graph)

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                dfs(i, j, graph)
                answer += 1

    return answer



for _ in range(T):
    print(testcase())
    