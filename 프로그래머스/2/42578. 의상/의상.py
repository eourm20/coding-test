from collections import Counter

def solution(clothes):
    answer = 1
    cnt_dict = Counter([kind for name, kind in clothes])
    for cnt in cnt_dict.values():
        answer *= cnt+1
    return answer-1

