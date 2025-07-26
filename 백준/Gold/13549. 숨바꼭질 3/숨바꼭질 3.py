import heapq
answer = 1
n, k = map(int, input().split())
time = [100001]*100001
time[n] = 0 # 내 위치
#할 수 있는 행동이 3개
after = []
after.append((0,n))
while after:
    # t, now = after.pop(0)
    t, now = heapq.heappop(after)
    if t > time[now]:
        continue
    if now == k:
        print(time[now])
        break
    for next in [now*2, now+1, now-1]:
        if 0<=next<=100000: #순서가 빨리 오는하는게 우선순위
            if next == now*2: #0초
                if t < time[next]:
                    time[next] = t
                    # after.append((t,next))
                    heapq.heappush(after, (t,next))
            else:
                if t+1 < time[next]:
                    time[next] = t+1
                    # after.append((t+1,next))
                    heapq.heappush(after,(t+1,next))