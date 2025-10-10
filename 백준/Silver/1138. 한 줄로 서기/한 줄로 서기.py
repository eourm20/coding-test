import sys
input = sys.stdin.readline

n = int(input())
info = list(map(int, input().split()))
line = [0] * n

for i in range(n):
    count = 0
    for j in range(n):
        if count == info[i] and line[j] == 0:
            line[j] = i + 1
            break
        if line[j] == 0:
            count += 1

print(*line)