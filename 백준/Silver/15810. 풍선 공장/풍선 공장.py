
import sys
input = sys.stdin.readline  # 빠른 입력

# answer 145
N, M = map(int, input().split())
A = list(map(int, input().split()))

left = 1
right = max(A)*M

while left<= right:
    balloon = 0
    mid = (left+right)//2
    for a in A:
        balloon+=mid//a
    if balloon<M:
        left = mid +1
    else:
        right = mid-1
        answer = mid

print(answer)