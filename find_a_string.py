s1 = "ABCDCDC"
s2 = "CDC"
L = len(s2)
count = 0
for i in range(len(s1)-(L-1)):
    slice_s1 = s1[i:i+L]
    if s2 == slice_s1:
        count += 1


print(count)

