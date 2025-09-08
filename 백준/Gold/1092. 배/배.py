import sys
input = sys.stdin.readline

c = int(input())
c_list = list(map(int, input().split()))
n = int(input())
n_list = list(map(int, input().split()))
c_list.sort(reverse=True)
n_list.sort(reverse=True)
# print(c_list, n_list)
if c_list[0] < n_list[0]:
    print(-1)
else:
    minutes = 0
    # 남은 박스 목록을 인덱스로 훑으며, 한 분마다 각 크레인이 하나씩 집는다.
    pos = [0] * c          # 각 크레인이 다음에 볼 박스 인덱스(되감지 않음)
    taken = [False] * n    # 박스 집혔는지 표시
    left = n               # 남은 박스 수

    while left > 0:
        moved = 0
        for i in range(c):
            # 이 크레인이 들 수 있는, 아직 안 집힌 박스를 찾을 때까지 전진
            while pos[i] < n and (taken[pos[i]] or n_list[pos[i]] > c_list[i]):
                pos[i] += 1
            if pos[i] < n:
                taken[pos[i]] = True
                pos[i] += 1
                left -= 1
                moved += 1
        minutes += 1

    print(minutes)