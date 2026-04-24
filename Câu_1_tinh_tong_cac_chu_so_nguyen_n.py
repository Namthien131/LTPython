def tong_chu_so(n):
    n = abs(n)

    if n == 0:
        return 0

    return n % 10 + tong_chu_so(n // 10)


n = int(input("Nhập n: "))
print("Tổng các chữ số là:", tong_chu_so(n))