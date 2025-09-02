  
def solution(name):
    change = 0
    # 알파벳 반, 13
    # 이름 반, int(len(name)//2)
    # 알파벳 변경
    for n in name:
        change += min(abs(ord('A')-ord(n)),abs(ord('Z')-ord(n))+1)
        # print(answer)
    # 이동 변경
    move = len(name) - 1
    for i in range(len(name)):
        next_idx = i + 1
        # 연속된 A 건너뛰기
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
        # i 지점까지 갔다가 돌아가서 끝으로 가는 경우 비교
        move = min(move, i * 2 + len(name) - next_idx, (len(name) - next_idx) * 2 + i)
    
    return change + move
 