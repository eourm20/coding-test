# 17503 맥주 축제

import sys
input = sys.stdin.readline  # 빠른 입력

# answer 5
N, M, K = map(int, input().split())
beers_luv = []
beers_al = []
for _ in range(K):
    v, c = tuple(map(int, input().split()))
    beers_luv.append(v)
    beers_al.append(c)
# print(beers_al)
answer = 0
left = 0
right = max(beers_al)
# print(right)
while left <= right:
    mid = (left+right)//2
    luv = 0
    luv_list = []
    for i in range(len(beers_luv)):
        if beers_al[i]<=mid:
            luv_list.append(beers_luv[i])
    if len(luv_list) < N:
        left = mid + 1
        continue
    luv = sum(sorted(luv_list)[-N:])
    if luv < M:
        left = mid + 1
        
    else:
        right = mid - 1
        answer = mid

print(answer if answer!=0 else -1)