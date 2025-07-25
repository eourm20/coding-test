import heapq
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range (n+1)]
    for s,f in edge:
        graph[s].append(f)
        graph[f].append(s)
    dist = [50000]*(n+1)
    dist[1] = 0
    heap = [(0,1)]
    # print(dist)
    
    while heap:
        dis, node = heapq.heappop(heap)
        if dis > dist[node]:
            continue
        # print('dis:', dis)
        # print('node:', node)
        # print(graph[node])
        # print(dist)
        for next_node in graph[node]:
            new_dis = dis+1
            if new_dis < dist[next_node]:
                dist[next_node] = new_dis
                heapq.heappush(heap,(new_dis,next_node))
    return sum(1 for d in dist[1:] if d == max(dist[1:]))