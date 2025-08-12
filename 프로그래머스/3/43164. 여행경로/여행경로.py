def solution(tickets):
    tickets.sort()
    visited = [False] * len(tickets)
    path = []
    result = []

    def dfs(curr, depth):
        nonlocal result
        path.append(curr)

        if depth == len(tickets):
            result = path[:]
            return True

        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == curr:
                visited[i] = True
                if dfs(tickets[i][1], depth + 1):
                    return True #바아아로 이어지면
                # 안이어지면! 나가리
                visited[i] = False

        path.pop()
        return False

    dfs("ICN", 0)
    return result