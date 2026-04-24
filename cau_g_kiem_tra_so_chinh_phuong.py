# Hàm kiểm tra n có là số chính phương hay không

import math

kiem_tra_chinh_phuong = lambda n: n >= 0 and int(math.sqrt(n)) ** 2 == n

n = int(input("Nhập n: "))

if kiem_tra_chinh_phuong(n):
    print(n, "là số chính phương")
else:
    print(n, "không là số chính phương")