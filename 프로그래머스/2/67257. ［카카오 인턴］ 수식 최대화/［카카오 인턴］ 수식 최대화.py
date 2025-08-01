import re
from itertools import permutations

def solution(expression):
    nums = list(map(int, re.findall(r'\d+', expression)))
    ops = re.findall(r'[\+\-\*]', expression)
    
    operators = list(set(ops))  # 연산자 확인
    answer = 0

    # permutations: 조합 생성하는 함수
    for priority in permutations(operators):
        n = nums.copy()
        o = ops.copy()
        
        for op in priority:
            i = 0
            while i < len(o):
                if o[i] == op:
                    if op == '+':
                        result = n[i] + n[i+1]
                    elif op == '-':
                        result = n[i] - n[i+1]
                    elif op == '*':
                        result = n[i] * n[i+1]
                    n[i] = result
                    # n.remove(n[i+1])
                    # o.remove(o[i])
                    del n[i+1]
                    del o[i]
                else:
                    i += 1
        
        # 이전 값과 비교
        answer = max(answer, abs(n[0]))
    
    return answer