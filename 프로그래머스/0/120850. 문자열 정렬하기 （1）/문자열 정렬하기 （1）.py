def solution(my_string):
    answer = []
    st = sorted(my_string)
    for s in st:
        if s.isdigit():
            answer.append(int(s))
    
    return answer