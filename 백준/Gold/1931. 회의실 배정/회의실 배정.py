import sys
input = sys.stdin.readline

n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]
info = [(x[0], x[1], x[1]-x[0]) for x in info]
info.sort(key=lambda x: (x[0], x[1]), reverse=(True, False))

answer = 1
s = 0
for i in range(s+1, n):
    if info[s][0] >= info[i][1]:
        answer += 1
        s = i

print(answer)