import sys
from collections import Counter
trees = sys.stdin.read().strip().split('\n')
counter = Counter(trees)
print_trees = list(set(trees))
print_trees.sort()
for i in range(len(print_trees)):
    # 주어진 각 종의 이름을 사전순으로 출력하고, 그 종이 차지하는 비율을 백분율로 소수점 4째자리까지 반올림해 함께 출력한다.
    print(f"{print_trees[i]} {counter[print_trees[i]]/len(trees)*100:.4f}")