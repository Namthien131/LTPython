# Hàm nhận bán kính r và tính diện tích hình tròn

import math

dien_tich_hinh_tron = lambda r: math.pi * r ** 2

r = float(input("Nhập bán kính r: "))

print("Diện tích hình tròn là:", dien_tich_hinh_tron(r))