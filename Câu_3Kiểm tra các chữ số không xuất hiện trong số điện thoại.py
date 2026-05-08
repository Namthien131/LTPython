S = input("Nhập số điện thoại: ")

khong_xuat_hien = []

for i in range(10):
    if str(i) not in S:
        khong_xuat_hien.append(i)

print("Trong số điện thoại", S, "không chứa các ký số:", khong_xuat_hien)