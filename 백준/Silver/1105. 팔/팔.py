import sys
input = sys.stdin.readline

l, r = map(int, input().split())

L = str(l)
R = str(r)

if len(L) != len(R):
    print(0)
else:
    answer = 0
    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i] == '8':
                answer += 1
        else:
            break
    print(answer)