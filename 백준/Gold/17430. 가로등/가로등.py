import sys
from collections import defaultdict, Counter

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    ys_by_x = defaultdict(list)
    for _ in range(N):
        x, y = map(int, input().split())
        ys_by_x[x].append(y)

    # x별로 y 멀티셋 Counter 생성
    counters = [Counter(v) for v in ys_by_x.values()]
    # print(ys_by_x)
    # print(counters)
    base = counters[0]
    ok = all(c == base for c in counters)

    print("BALANCED" if ok else "NOT BALANCED")