def solution(numbers, target):
    answer = 0
    
    stack = []
    stack.append((0, 0))  # (현재 인덱스, 누적 합)

    while stack:
        idx, total = stack.pop()  # DFS는 스택: 후입선출

        if idx == len(numbers):
            if total == target:
                answer += 1
            continue

        stack.append((idx + 1, total + numbers[idx]))  # + 선택
        stack.append((idx + 1, total - numbers[idx]))  # - 선택
    return answer