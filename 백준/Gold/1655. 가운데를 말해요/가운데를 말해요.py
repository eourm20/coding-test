import sys
import heapq
input = sys.stdin.readline

N = int(input())
left = []
right = []

for _ in range(N):
    x = int(input())

    if not left or x <= -left[0]:
        heapq.heappush(left, -x)
    else:
        heapq.heappush(right, x)

    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(right) > len(left):
        heapq.heappush(left, -heapq.heappop(right))

    print(-left[0])