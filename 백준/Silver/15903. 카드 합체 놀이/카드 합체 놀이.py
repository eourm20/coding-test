import sys
import heapq
input = sys.stdin.readline

N, T = map(int, input().split())

cards = list(map(int, input().split()))
cards.sort()

for _ in range(T):
    sub_sum = cards[0] + cards[1]
    cards[0] = sub_sum
    cards[1] = sub_sum
    cards.sort()
# print(cards)
print(sum(cards))