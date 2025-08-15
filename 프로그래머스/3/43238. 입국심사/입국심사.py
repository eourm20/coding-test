def solution(n, times):
    answer = 0
    min_t = 0
    max_t = max(times)*n
    while min_t <= max_t:
        print('min:', min_t)
        print('max:', max_t)
        mid_t = (min_t+max_t)//2
        print('mid_t:',mid_t)
        complete_n = sum(mid_t//t for t in times)
        print('complete_n:',complete_n)
        if complete_n >= n:
            answer = mid_t
            max_t = mid_t-1
        else:
            min_t = mid_t+1
        
    return answer