S = input("Nhập chuỗi: ")

ds_tu = S.split()

ket_qua = None

for i in range(len(ds_tu)):
    for j in range(i + 1, len(ds_tu)):
        if ds_tu[i] == ds_tu[j]:
            ket_qua = ds_tu[i]
            break

    if ket_qua is not None:
        break

print(ket_qua)