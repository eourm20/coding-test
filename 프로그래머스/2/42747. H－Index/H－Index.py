def solution(citations):
    answer = 0
    citations = sorted(citations)
    print(citations)
    for h in range(len(citations)+1):
        best_paper = sum(1 for c in citations if c >= h)
        if best_paper >= h:
            answer = h
    return answer