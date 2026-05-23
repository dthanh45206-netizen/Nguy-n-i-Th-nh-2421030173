day = "1 2 3 4 5 6"

tong = 0

for i in day.split():
    if int(i) % 2 == 0:
        tong = tong + int(i)

print(tong)