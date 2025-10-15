import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '*':
        break
    D = len(s)
    ment = 'is surprising.'
    for i in range(D-1):
        seen = set()
        for j in range(D-i-1):
            pair = (s[j], s[j+i+1])
            if pair in seen:
                ment = 'is NOT surprising.'
                break
            seen.add(pair)
        if ment == 'is NOT surprising.':
            break
    print(f"{s} {ment}")
