import sys
input = sys.stdin.readline

n = int(input())
g = [int(input()) for _ in range(n)]
answer = []

if n == 1:
    # 정의에 따라 단일 원소를 포함할지 결정
    answer.append(1)
else:
    # 첫 원소
    if g[0] >= g[1]:
        answer.append(1)

    # 가운데 구간
    for i in range(1, n-1):
        if g[i-1] <= g[i] and g[i] >= g[i+1]:
            answer.append(i+1)

    # 마지막 원소
    if g[-1] >= g[-2]:
        answer.append(n)

for a in answer:
    print(a)