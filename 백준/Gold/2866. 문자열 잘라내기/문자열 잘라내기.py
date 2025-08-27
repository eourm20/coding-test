import sys
input = sys.stdin.readline

R, C = map(int, input().split())
s = [[] for _ in range(R)]
S = [input().strip() for _ in range(R)]
s = [''.join(row[c] for row in S) for c in range(C)]

count = 0
for k in range(1,R):
    new = []
    for ss in s:
        new.append(ss[k-count:])
        
    if len(set(new)) != C:
        break
    else:
        count += 1
        s = new
print(count)