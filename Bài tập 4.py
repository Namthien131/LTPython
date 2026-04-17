n = int(input("Nhập số nguyên dương n: "))

chan = 0
le = 0
tam = n

while tam > 0:
    chu_so = tam % 10
    if chu_so % 2 == 0:
        chan += 1
    else:
        le += 1
    tam //= 10

print("Số lượng số lẻ:", le)
print("Số lượng số chẵn:", chan)