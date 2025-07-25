import heapq

def solution(N, road, K):
    city = [[] for _ in range(N + 1)]
    for s, f, d in road:
        city[s].append((f, d))
        city[f].append((s, d))

    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    heap = [(0, 1)]  # (거리, 현재 마을)

    while heap:
        dis, node = heapq.heappop(heap)
        if dis > dist[node]:
            continue
        for next_node, next_dis in city[node]:
            new_dis = dis + next_dis
            if new_dis < dist[next_node]:
                dist[next_node] = new_dis
                heapq.heappush(heap, (new_dis, next_node))

    return sum(1 for d in dist if d <= K)