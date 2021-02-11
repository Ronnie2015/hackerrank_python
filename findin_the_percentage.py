
n = int(input())

students_marks = {}

for _ in range(n):
    name, *line = input().split()
    score = list(map(float, line))
    students_marks[name] = sum(score)/len(score)

print(students_marks)
query_name = str(input())
print("%.2f" %students_marks[query_name])



