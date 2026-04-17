n = int(input("Nhập số nguyên dương n: "))

tong = 0
tich = 1
tam = n

while tam > 0:
    chu_so = tam % 10
    tong += chu_so
    tich *= chu_so
    tam //= 10

print("Tổng =", tong)
print("Tích =", tich)