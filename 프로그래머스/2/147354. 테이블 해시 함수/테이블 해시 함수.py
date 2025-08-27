def solution(data, col, row_begin, row_end):
    new_data = sorted(data,key=lambda x: (x[col-1] if col != 0 else x[col], -x[0])
)
    result = []
    for i in range(row_begin-1, row_end):
        sub_result = []
        for value in new_data[i]:
            sub_result.append(value % (i+1))
        # print(sub_result)
        result.append(sum(sub_result))
    # print(result)
    answer = result[0]
    for a in result[1:]:
        answer ^= a
    return answer