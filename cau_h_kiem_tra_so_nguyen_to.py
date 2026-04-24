# Hàm kiểm tra n có là số nguyên tố hay không

import math

kiem_tra_nguyen_to = lambda n: n > 1 and all(
    n % i != 0 for i in range(2, int(math.sqrt(n)) + 1)
)

n = int(input("Nhập n: "))

if kiem_tra_nguyen_to(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không là số nguyên tố")