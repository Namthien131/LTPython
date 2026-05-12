# Danh sách mệnh giá tiền
menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]

# Nhập số tiền cần trả và số tiền khách đưa
a = int(input("Nhap so tien can thanh toan: "))
b = int(input("Nhap so tien khach dua: "))

# Trường hợp khách đưa thiếu tiền
if a > b:
    print(f"Khach con thieu {a - b} dong")

# Trường hợp khách đưa đúng tiền
elif a == b:
    print("Cam on khach hang. Hen gap lai")

# Trường hợp cần thối tiền
else:
    tien_thoi = b - a

    print(f"\nSo tien can thoi lai: {tien_thoi}")

    tong_to = 0
    tong_loai = 0

    print("\nDoi thanh:")

    for tien in menh_gia:
        so_to = tien_thoi // tien
        tien_thoi = tien_thoi % tien

        # Chỉ in loại tiền có số tờ > 0
        if so_to > 0:
            print(f"Loai {tien} gom {so_to} to")
            tong_loai += 1

        tong_to += so_to

    print(f"\nTONG CONG CO {tong_to} TO")
    print(f"Tong so loai = {tong_loai}")

    input("\nNhan Enter de ket thuc...")

    print("Cam on khach hang. Hen gap lai")