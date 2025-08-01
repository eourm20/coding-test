# 섬 연결하기
import heapq
def solution(n, costs):
    visited = [False] * n
    map = [[] for _ in range(n)]
    for a, b, cost in costs:
        map[a].append((cost, b))
        map[b].append((cost, a))
    
    answer = 0
    heap = [(0, 0)]  # (cost, start_node)

    while heap:
        cost, node = heapq.heappop(heap)
        if visited[node]:
            continue
        visited[node] = True
        answer += cost

        for next_cost, next_node in map[node]:
            if not visited[next_node]:
                heapq.heappush(heap, (next_cost, next_node))

    return answer