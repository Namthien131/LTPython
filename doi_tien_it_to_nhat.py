# Danh sách các loại tiền
menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]

# Nhập số tiền X
x = int(input("Nhap so tien X: "))

tong_to = 0

print(f"\nSo tien {x} duoc doi thanh:")

# Đổi tiền
for tien in menh_gia:
    so_to = x // tien
    x = x % tien

    print(f"Loai {tien} gom {so_to} to")

    tong_to += so_to

print(f"\nTONG CONG CO {tong_to} TO")