import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = sorted(map(int, input().split()))
    arr_set = set(arr)  # O(N)
    answer = 0

    for i in range(N - 2):
        for k in range(i + 2, N):
            if (arr[i] + arr[k]) % 2 == 0:
                mid = (arr[i] + arr[k]) // 2
                if mid in arr_set:
                    answer += 1

    print(answer)
