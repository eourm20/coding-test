import sys
input = sys.stdin.readline

k, n = map(int, input().split())
a = [int(input()) for _ in range(k)]
a.sort()
s = 1
e = a[-1]
while s <= e:
    m = (s + e) // 2
    cnt = 0
    for i in a:
        cnt += i // m
    if cnt >= n:
        s = m + 1
    else:
        e = m - 1
print(e)