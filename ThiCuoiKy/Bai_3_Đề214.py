
import math

la_so_chinh_phuong = lambda n: n > 0 and int(math.sqrt(n)) ** 2 == n

kiem_tra_tam_giac = lambda a, b, c: a + b > c and a + c > b and b + c > a

phan_loai_tam_giac = lambda a, b, c: (
    "Tam giác đều" if a == b == c else
    "Tam giác vuông cân" if (
        (a == b or a == c or b == c) and
        (a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a)
    ) else
    "Tam giác cân" if a == b or a == c or b == c else
    "Tam giác vuông" if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a else
    "Tam giác thường"
)

# Trường hợp 1: kiểm tra số chính phương
n = int(input("Nhập số nguyên n: "))

if la_so_chinh_phuong(n):
    print(n, "là số chính phương")
else:
    print(n, "không phải là số chính phương")

# Trường hợp 2: kiểm tra và phân loại tam giác
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

if kiem_tra_tam_giac(a, b, c):
    print(a, b, c, "là 3 cạnh hợp lệ của tam giác")
    print("Loại tam giác:", phan_loai_tam_giac(a, b, c))
else:
    print(a, b, c, "không phải là 3 cạnh hợp lệ của tam giác")