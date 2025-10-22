import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))
stack = []  # (index, height)
answer = []

for i in range(n):
    h = heights[i]

    # 스택의 top이 현재 탑보다 낮으면 pop
    while stack and stack[-1][1] < h:
        stack.pop()

    # 스택이 비어 있으면 수신할 탑이 없음 → 0
    if not stack:
        answer.append(0)
    else:
        answer.append(stack[-1][0])  # 수신할 탑의 번호(index)

    # 현재 탑을 스택에 push
    stack.append((i + 1, h))

print(*answer)