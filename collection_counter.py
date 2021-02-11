from collections import Counter
X = int(input())
stock = list(map(int, input().split(' ')))
Dict = Counter(stock)
p = 0
for _ in range(int(input())):
    size, price = map(int, input().split(' '))
    if Dict[size]:
        Dict[size] -= 1
        p += price

print(p)

