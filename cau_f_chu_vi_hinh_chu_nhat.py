# Hàm nhận chiều dài d, chiều rộng r và tính chu vi hình chữ nhật

chu_vi_hinh_chu_nhat = lambda d, r: 2 * (d + r)

d = float(input("Nhập chiều dài: "))
r = float(input("Nhập chiều rộng: "))

print("Chu vi hình chữ nhật là:", chu_vi_hinh_chu_nhat(d, r))