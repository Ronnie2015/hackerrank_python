# list comprehension
x = int(input())
y = int(input())
z = int(input())
n = int(input())
x, y, z = x+1, y+1, z+1
# append method
myList = []
for i in range(x):
    for j in range(y):
        for k in range(z):
            if (i+j+k) !=n:
                myList.append([i, j, k])

# comprehension method
myList2 = [[i, j, k] for i in range(x) for j in range(y) for k in range(z) if (i+j+k) !=n]
print(myList)
print(myList2)
