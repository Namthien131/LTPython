# Hàm nhận 1 số nguyên n và trả về trị tuyệt đối của n + 15

tri_tuyet_doi_n_cong_15 = lambda n: abs(n + 15)

n = int(input("Nhập n: "))

print("Trị tuyệt đối của n + 15 là:", tri_tuyet_doi_n_cong_15(n))