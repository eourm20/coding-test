from collections import deque
n, m = map(int, input().split())
maze = []
for _ in range(n):
    row = []
    for a in input():
        row.append(int(a))
    maze.append(row)
r = 0
c = 0
r_list = [-1,1,0,0]
c_list = [0,0,-1,1]
queue = deque()
queue.append((0, 0))

while queue:
    r, c = queue.popleft()
    for i in range(4):
        cur_r = r + r_list[i]
        cur_c = c + c_list[i]

        if 0 <= cur_r < n and 0 <= cur_c < m and maze[cur_r][cur_c] == 1:
            maze[cur_r][cur_c] = maze[r][c] + 1
            queue.append((cur_r, cur_c))

print(maze[n-1][m-1])