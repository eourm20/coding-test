def solution(m, n, puddles):
    answer = 0
    map = [[0] * m for _ in range (n)]
    map[0][0] = 1
    print(map)
    
    for i in range(m):
        for j in range(n):
            if [i,j] == [0,0]:
                continue
            if [i+1,j+1] in puddles:
                map[j][i] = 0
            else:
                # 위에서 오는거 / 왼쪽에서 오는거
                map[j][i] = ((map[j-1][i] + map[j][i-1]))%1000000007
            
    return map[n-1][m-1]