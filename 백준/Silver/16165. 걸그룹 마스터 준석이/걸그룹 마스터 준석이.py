import sys
input = sys.stdin.readline

N, M = map(int, input().split())
group = {}
member = {}

for _ in range(N):
    g = input().strip()
    member_count = int(input())
    members = [input().strip() for _ in range(member_count)]

    group[g] = members
    for m in members:
        member[m] = g

for _ in range(M):
    quiz = input().strip()
    quiz_type = int(input())

    if quiz_type == 0:
        for name in sorted(group[quiz]):
            print(name)
    else:
        print(member[quiz])
