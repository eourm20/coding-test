import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))
M = sum(arr)
# print(M)
answer = set()
for i in range(1, n+1):
    for j in combinations(arr, i):
        # print(j)
        if sum(j) <= M and sum(j) >= 1:
            answer.add(sum(j))
print(M-len(answer))