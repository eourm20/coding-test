import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

l, r = 0, n - 1
answer = abs(a[l] + a[r])
ans = [a[l], a[r]]

while l < r:
    s = a[l] + a[r]

    if abs(s) < answer:
        answer = abs(s)
        ans = [a[l], a[r]]

    if s < 0:
        l += 1
    else:
        r -= 1

print(*ans)
