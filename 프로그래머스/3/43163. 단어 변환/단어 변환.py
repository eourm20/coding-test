from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    queue = deque()
    queue.append((0,begin))
    visited = set()
    while queue:
        c,b = queue.popleft()
        print(c, b)
        if b == target:
            return c
        for word in words:
            if word not in visited and sum(x != y for x, y in zip(b, word)) == 1:
                visited.add(word)
                queue.append((c + 1, word))  
    
    return answer