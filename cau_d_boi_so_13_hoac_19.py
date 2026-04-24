# Hàm kiểm tra n có là bội số của 13 hoặc 19 hay không

kiem_tra_boi_so = lambda n: n % 13 == 0 or n % 19 == 0

n = int(input("Nhập n: "))

if kiem_tra_boi_so(n):
    print(n, "là bội số của 13 hoặc 19")
else:
    print(n, "không là bội số của 13 hoặc 19")