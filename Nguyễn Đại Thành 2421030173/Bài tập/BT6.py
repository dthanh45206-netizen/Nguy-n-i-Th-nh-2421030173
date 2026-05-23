day = "-5 -20 -50 10 -1001 -30"

tong = 0
dem = 0

for i in day.split():
    if -1000 < float(i) < -10:
        tong = tong + float(i)
        dem = dem + 1

if dem > 0:
    print(tong / dem)
else:
    print("Không có số nào thỏa mãn điều kiện")