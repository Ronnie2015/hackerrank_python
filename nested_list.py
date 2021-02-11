result = []
for _ in range(int(input())):
    name = str(input())
    score = float(input())
    result.append([name, score])

score = sorted(set([x[1] for x in result]))

for name in sorted([x[0] for x in result if x[1]==score[1]]):
    print(name)




