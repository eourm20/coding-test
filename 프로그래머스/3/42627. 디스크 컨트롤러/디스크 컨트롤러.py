import heapq

def solution(jobs):
    jobs.sort()
    time = 0
    total_time = 0
    idx = 0
    heap = []
    count = len(jobs)

    while idx < count or heap:
        while idx < count and jobs[idx][0] <= time: #요청시간 안에 들어옴
            heapq.heappush(heap, (jobs[idx][1], jobs[idx][0]))
            idx += 1
        
        if heap:
            work, start = heapq.heappop(heap)
            time += work
            total_time += time - start
        else:
            # 요청 시간 안겹치면 바로 다음 작업
            time = jobs[idx][0]
    
    return total_time // count