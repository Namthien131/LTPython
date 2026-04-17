n = int(input("Nhập số nguyên dương n: "))

tam = n
may_man = True

while tam > 0:
    chu_so = tam % 10
    if chu_so != 6 and chu_so != 8:
        may_man = False
        break
    tam //= 10

if may_man:
    print(n, "là số may mắn")
else:
    print(n, "không phải là số may mắn")