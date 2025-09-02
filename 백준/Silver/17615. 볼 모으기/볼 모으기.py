import sys
input = sys.stdin.readline

N = int(input())
balls = input()
# 빨간공
red_check1 = 0
red_check2 = 0
pre1 = ""
pre2 = ""
for i in range(len(balls)):
    if balls[i] == 'R':
        if pre1 == "B":
            red_check1 += 1
    
    if balls[-i-1] == 'R':
        if pre2 == "B":
            red_check2 += 1
    pre1 = 'B' if balls[i] == 'R' and pre1 == "B" else balls[i]
    pre2 = 'B' if balls[-i-1] == 'R' and pre2 == "B" else balls[-i-1]
# print(red_check1, red_check2)

# 파란공
blue_check1 = 0
blue_check2 = 0
blue_pre1 = ""
blue_pre2 = ""
for i in range(len(balls)):
    if balls[i] == 'B':
        if blue_pre1 == "R":
            blue_check1 += 1
    
    if balls[-i-1] == 'B':
        if blue_pre2 == "R":
            blue_check2 += 1
    blue_pre1 = 'R' if balls[i] == 'B' and blue_pre1 == "R" else balls[i]
    blue_pre2 = 'R' if balls[-i-1] == 'B' and blue_pre2 == "R" else balls[-i-1]
print(min(blue_check1, blue_check2, red_check1, red_check2))
