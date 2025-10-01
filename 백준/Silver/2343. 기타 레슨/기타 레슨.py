import sys
input = sys.stdin.readline

n, m = map(int, input().split())
streams = list(map(int, input().split()))

start, end = max(streams), sum(streams )
answer = end

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    total = 0
    for stream in streams:
        if total + stream > mid:
            cnt += 1
            total = 0
        total += stream
    if cnt <= m:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)