import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    gift = str(input().rstrip())
    # print(gift)
    if len(heap)==0:
        if gift == '0':
            print(-1)
        else:
            add_gift = list(map(int, gift.split()))
            for i in range(1, add_gift[0]+1):
                heapq.heappush(heap, -add_gift[i])
    else:
        if gift == '0':
            print(-heapq.heappop(heap))
        else:
            add_gift = list(map(int, gift.split()))
            for i in range(1, add_gift[0]+1):
                heapq.heappush(heap, -add_gift[i])