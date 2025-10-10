import sys
input = sys.stdin.readline

number = 1
while True:
    s = input().rstrip()
    if '-' in s:
        break
    
    ss = []
    change = 0
    
    for ch in range(len(s)):
        # if ch == 0:
        #     if s[ch] == '}':
        #         change += 1
        #         ss.append('{')
        #     else:
        #         ss.append('{')
        # else:
        if s[ch] == '{':
            ss.append('{')
        elif s[ch] == '}':
            if len(ss) != 0:
                ss.pop()
            else:
                change += 1
                ss.append('{')
                    
    # print(ss)
    change += len(ss)//2
    print(f"{number}. {change}")
    number += 1
