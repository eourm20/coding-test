def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    # print(rocks)
    left = 1
    right = distance
    
    while left <= right:
        mid = (left+right) //2
        remove = 0
        prev = 0
        for r in rocks:
            if r - prev < mid:
                remove += 1
            else:
                prev = r
                
        if remove <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid -1
            
    
#     for i in range(len(rocks)):
#         if i == 0:
#             left.append(rocks[i]-0)
        
#         else:
#             left.append(rocks[i]-rocks[i-1])
#             if i == len(rocks)-1:
#                 left.append(distance-rocks[-1])
#     print(left)

    return answer