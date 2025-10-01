import sys
input = sys.stdin.readline

n = int(input())
cost = list(map(int, input().split()))
total_cost = int(input())

if sum(cost) <= total_cost:
    print(max(cost))
    exit()

s = 0
e = max(cost)
answer = 0

while s <= e:
    m = (s + e) // 2
    t = 0
    for c in cost:
        t += min(c, m)

    if t > total_cost:
        e = m - 1
    else:
        answer = m
        s = m + 1

print(answer)