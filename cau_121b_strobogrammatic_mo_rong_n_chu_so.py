def sinh_strobogrammatic_mo_rong(n, tong_do_dai):

    if n == 0:
        return [""]

    if n == 1:
        return ["0", "1", "2", "5", "8"]

    ds = sinh_strobogrammatic_mo_rong(n - 2, tong_do_dai)

    ket_qua = []

    for s in ds:

        if n != tong_do_dai:
            ket_qua.append("0" + s + "0")

        ket_qua.append("1" + s + "1")
        ket_qua.append("2" + s + "2")
        ket_qua.append("5" + s + "5")
        ket_qua.append("6" + s + "9")
        ket_qua.append("8" + s + "8")
        ket_qua.append("9" + s + "6")

    return ket_qua


n = int(input("Nhap n (2 <= n <= 10): "))

if 2 <= n <= 10:

    print(f"Cac so strobogrammatic mo rong gom {n} chu so:")

    ket_qua = sinh_strobogrammatic_mo_rong(n, n)

    for so in ket_qua:
        print(so)

else:
    print("n khong hop le")