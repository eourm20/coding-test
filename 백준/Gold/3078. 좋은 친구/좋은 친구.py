import sys
input = sys.stdin.readline
from collections import deque
N, K  = map(int, input().split())
students = [len(input().rstrip()) for _ in range(N)]
q = [deque() for _ in range(21)]
f = 0
for i in range(N):
    stu = students[i]
    # print('stu:', stu)
    while q[stu] and i - q[stu][0] > K:
        q[stu].popleft()
    # print('q', q)
        
    f += len(q[stu])
    q[stu].append(i)

print(f)