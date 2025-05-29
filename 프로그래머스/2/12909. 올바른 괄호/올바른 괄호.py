def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        if len(stack)==0 and s[i]==")":
            return False
        elif s[i]=="(":
            stack.append(s[i])
        else:
            stack.pop()
    if len(stack)==0:
        return True
    else:
        return False
