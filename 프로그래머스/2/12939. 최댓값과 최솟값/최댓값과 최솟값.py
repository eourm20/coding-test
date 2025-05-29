def solution(s):
    arr = list(map(int,s.split()))
    answer = ' '.join(map(str,[min(arr), max(arr)]))
    return answer