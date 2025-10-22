import sys
input = sys.stdin.readline

N = int(input())
a = [tuple(map(int, input().split())) for _ in range(N)]
a.sort()

max_h = max(a, key=lambda x: x[1])
max_idx = a.index(max_h)

# 왼쪽
area = 0
left_x, left_h = a[0]
for i in range(1, max_idx + 1):
    x, h = a[i]
    if h >= left_h:
        area += (x - left_x) * left_h
        left_x, left_h = x, h

# 오른쪽
right_x, right_h = a[-1]
for i in range(N - 2, max_idx - 1, -1):
    x, h = a[i]
    if h >= right_h:
        area += (right_x - x) * right_h
        right_x, right_h = x, h

area += max_h[1]

print(area)