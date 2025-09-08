import sys
input = sys.stdin.readline
import heapq

N, K = map(int, input().split())
j = [tuple(map(int, input().split())) for _ in range(N)]
b = [int(input()) for _ in range(K)]

j.sort(key=lambda x: x[0])
b.sort()

answer = 0
pq = []
idx = 0   

for bb in b:
    while idx < N and j[idx][0] <= bb:
        heapq.heappush(pq, -j[idx][1])
        idx += 1
    if pq:
        answer += -heapq.heappop(pq)

print(answer)