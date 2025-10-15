import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
lines = []
nodes = defaultdict(list)

for i in range(n):
    arr = list(map(int, input().split()))[1:]
    lines.append(arr)
    for a in arr:
        nodes[a].append(i)

# print('line', lines)
# print('node', nodes)
goal = int(input())

stack = deque()
visited_line = set()
visited_node = set()

# 0번 역부터 시작
for line in nodes[0]:
    stack.append((line, 0))
    visited_line.add(line)
    visited_node.add(0)
    
while stack:
    line, change = stack.popleft()
    # print('line, change', line, change)
    if goal in lines[line]:
        print(change)
        break
    
    for node in lines[line]:
        if node in visited_node:
            continue
        visited_node.add(node)
        
        for next_node in nodes[node]:
            if next_node not in visited_line:
                visited_line.add(next_node)
                stack.append((next_node, change+1))
        # print('visited_line', visited_line)
        # print('visited_node', visited_node)
else:
    print(-1)
