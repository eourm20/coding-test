def solution(triangle):
    # 아래에서 위로 큰 값 따라가기
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            # 아래 두 개 중 큰 값
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    
    return triangle[0][0]