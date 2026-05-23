s = "2 4 6 7 9"

a = s.split()

for i in range(len(a)):
    a[i] = int(a[i])

print(a)