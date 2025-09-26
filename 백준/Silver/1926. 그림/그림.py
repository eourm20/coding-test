import sys
input = sys.stdin.readline

N, M= map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def dfs(i, j, graph):
    graph[i][j] = 0
    stack = [(i,j)]
    area = 1
    
    while stack:
        r, c = stack.pop()
        for dr, dc in ((1,0),(0,1),(0,-1),(-1,0)):
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<M and graph[nr][nc]==1:
                graph[nr][nc]=0
                area+=1
                stack.append((nr,nc))
    return area
    
    
biggest_paint = 0
paint_number = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            area = dfs(i, j, graph)
            paint_number += 1
            biggest_paint = max(biggest_paint, area)
            
print(paint_number)
print(biggest_paint)