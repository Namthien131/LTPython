import math

la_so_chinh_phuong = lambda n: int(math.sqrt(n)) ** 2 == n

la_so_hoan_thien = lambda n: n > 1 and sum(
    i for i in range(1, n)
    if n % i == 0
) == n

print("Các số chính phương từ 1 đến 10000 là:")
for i in range(1, 10001):
    if la_so_chinh_phuong(i):
        print(i, end=" ")

print("\n\nCác số hoàn thiện từ 1 đến 10000 là:")
for i in range(1, 10001):
    if la_so_hoan_thien(i):
        print(i, end=" ")