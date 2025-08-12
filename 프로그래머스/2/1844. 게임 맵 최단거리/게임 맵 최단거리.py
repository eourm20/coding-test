from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = 0
    r_list = [-1,1,0,0]
    c_list = [0,0,-1,1]
    queue = deque()
    queue.append((0, 0))

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            cur_r = r + r_list[i]
            cur_c = c + c_list[i]

            if 0 <= cur_r < n and 0 <= cur_c < m and maps[cur_r][cur_c] == 1:
                maps[cur_r][cur_c] = maps[r][c] + 1
                queue.append((cur_r, cur_c))

    return maps[n-1][m-1] if maps[n-1][m-1]!=1 else -1