import sys
input = sys.stdin.readline

k, n = map(int, input().split())
students = {}

for _ in range(n):
    s = input().strip()
    if s in students:
        del students[s]
    students[s] = True

for student in list(students.keys())[:k]:
    print(student)
