def solution(n, computers):
    visited = [False] * n

    def dfs(cur):
        visited[cur] = True
        for next in range(n):
            if computers[cur][next] == 1 and not visited[next]:
                dfs(next)
    
    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            print(visited)
            answer += 1
    return answer