def solution(number, k):
    stack = []
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
            # print('if',stack)
        stack.append(num)
        # print('ap',stack)
    return "".join(stack[:len(number)-k])