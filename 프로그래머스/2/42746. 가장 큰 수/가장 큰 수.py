def solution(numbers):
    arr = list(map(str, numbers))
    # print(arr)
    answer = ''
    arr.sort(key=lambda x: x * 4, reverse=True)
    res = ''.join(arr)
    return '0' if res[0] == '0' else res