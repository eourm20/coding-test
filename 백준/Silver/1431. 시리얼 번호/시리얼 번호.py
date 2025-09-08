import sys
input = sys.stdin.readline

n = int(input())
g = [input().rstrip() for _ in range(n)]
g.sort(key=lambda x: (len(x),sum(int(a) for a in x if a.isdigit()), x))
for gg in g:
    print(gg)