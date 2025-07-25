import heapq


def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    for ss, ff in roads:
        graph[ss].append((ff, 1))
        graph[ff].append((ss, 1))
    
    
    distance = [100000]*(n+1)
    distance[destination] = 0
    heap = [(0, destination)]
    while heap:
        dis, node = heapq.heappop(heap)
        if dis > distance[node]:
            continue
        for next_n, next_d in graph[node]:
            new_dis = dis+next_d
            if new_dis < distance[next_n]:
                distance[next_n] = new_dis
                heapq.heappush(heap, (new_dis, next_n))
    # print(distance)
    # return (distance[f] if distance[f] != 100000 else -1)


    for source in sources:
        answer.append(distance[source] if distance[source] != 100000 else -1)
    
    return answer