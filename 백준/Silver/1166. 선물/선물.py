import sys
input = sys.stdin.readline

n,l,w,h = map(int, input().split())
a_s, a_e = 0, min(l, w, h)

for _ in range(100):
    a_m = (a_s + a_e) / 2
    cnt = 1
    for i in [l, w, h]:
        cnt *= int(i / a_m)
    if cnt >= n:
        a_s = a_m
    else:
        a_e = a_m

print(a_s)