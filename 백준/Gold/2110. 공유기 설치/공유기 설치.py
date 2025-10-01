import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
l, r = 1, arr[-1] - arr[0]
answer = 0
while l <= r:
    mid = (l + r) // 2
    cnt = 1
    cur = arr[0]
    for i in range(1, n):
        if arr[i] >= cur + mid:
            cnt += 1
            cur = arr[i]
    if cnt >= c:
        answer = mid
        l = mid + 1
    else:
        r = mid - 1
print(answer)