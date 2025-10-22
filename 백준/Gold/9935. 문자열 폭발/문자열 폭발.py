import sys
input = sys.stdin.readline

string = input().rstrip()
boom = input().rstrip()
stack = []
for ch in string:
    stack.append(ch)
    if len(stack)>=len(boom):
        # print(''.join(stack[-len(boom):]))
        if ''.join(stack[-len(boom):]) == boom:
            # stack = stack[:len(stack)-len(boom)]
            del stack[-len(boom):]

answer = ''.join(stack) if stack else 'FRULA'
print(answer)