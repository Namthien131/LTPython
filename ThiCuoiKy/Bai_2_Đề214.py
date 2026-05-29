
def la_so_nguyen_to(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True


def tong_so_nguyen_to_nho_hon(n):
    tong = 0
    
    for i in range(2, n):
        if la_so_nguyen_to(i):
            tong += i
    
    return tong


def uoc_la_so_nguyen_to(n):
    danh_sach = []
    
    for i in range(1, n + 1):
        if n % i == 0 and la_so_nguyen_to(i):
            danh_sach.append(i)
    
    return danh_sach


n = int(input("Nhập số nguyên dương n: "))

if la_so_nguyen_to(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không phải là số nguyên tố")

print("Tổng các số nguyên tố nhỏ hơn", n, "là:", tong_so_nguyen_to_nho_hon(n))

print("Các ước của", n, "là số nguyên tố:", end=" ")
for x in uoc_la_so_nguyen_to(n):
    print(x, end=" ")