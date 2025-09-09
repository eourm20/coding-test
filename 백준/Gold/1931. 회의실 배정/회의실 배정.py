import sys
input = sys.stdin.readline

n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]
info.sort(key=lambda x: (x[0], x[1]), reverse=(True, False))
# ❌ Actual Output:
# [(12, 14, 2), (8, 11, 3), (8, 12, 4), (6, 10, 4), (5, 7, 2), (5, 9, 4), (3, 5, 2), (3, 8, 5), (2, 13, 11), (1, 4, 3), (0, 6, 6)]
answer = 1
s = 0
for i in range(s+1, n):
    if info[s][0] >= info[i][1]:
        answer += 1
        s = i

    
print(answer)