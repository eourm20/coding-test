def solution(s):
    no_single = ''
    answer = ''
    for a in s:
        if (a in answer) == False:
            answer +=a
        else:
            if a in no_single:
                pass
            else:
                no_single+=a
    
    # print(''.join(sorted(char for char in answer if char not in no_single)))
    answer = ''.join(sorted(char for char in answer if char not in no_single))
    return answer