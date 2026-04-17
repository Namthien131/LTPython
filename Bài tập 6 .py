n = int(input("Nhập số nguyên dương n: "))

tam = n
lon_nhat = 0

while tam > 0:
    chu_so = tam % 10
    if chu_so > lon_nhat:
        lon_nhat = chu_so
    tam //= 10

print("Số lớn nhất =", lon_nhat)