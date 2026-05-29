dai = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))

dien_tich_day = dai * rong
chu_vi_day = 2 * (dai + rong)
dien_tich_xung_quanh = chu_vi_day * cao
dien_tich_toan_phan = dien_tich_xung_quanh + 2 * dien_tich_day
the_tich = dai * rong * cao

print("Số lượng số lẻ cần hiển thị:", int(dai))
print(f"Diện tích đáy hình chữ nhật = {dien_tich_day:.2f} cm\u00b2")
print(f"Diện tích xung quanh hình khối = {dien_tich_xung_quanh:.2f} cm\u00b2")
print(f"Diện tích toàn phần hình khối = {dien_tich_toan_phan:.2f} cm\u00b2")
print(f"Thể tích hình khối = {the_tich:.2f} cm\u00b3")