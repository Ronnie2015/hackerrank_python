n, h = map(int, input().split())

s =".|."
m = n//2
for i in range(m):
    print((s*(i*2+1)).center(h, "-"))

if n//2 == m:
    print(("WELCOME").center(h, "-"))

for j in range(m-1, -1, -1):
    print((s*(j*2+1)).center(h, "-"))
