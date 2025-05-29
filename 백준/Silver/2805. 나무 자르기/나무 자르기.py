import sys
n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
bring_m = 0
min_m = 0
max_m = max(trees)
while min_m <= max_m:
    bring_m = 0
    mid_m = (max_m+min_m)//2
    bring_m = sum(tree - mid_m for tree in trees if tree > mid_m)
    if bring_m >= m:
        answer = mid_m
        min_m = mid_m+1
    else:
        max_m = mid_m-1
        
print(answer)