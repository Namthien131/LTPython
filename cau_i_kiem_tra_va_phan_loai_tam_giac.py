# Hàm kiểm tra 3 cạnh có tạo thành tam giác hay không
# Nếu có thì phân loại tam giác

phan_loai_tam_giac = lambda a, b, c: (
    "Không phải tam giác"
    if a + b <= c or a + c <= b or b + c <= a
    else "Tam giác đều"
    if a == b == c
    else "Tam giác vuông cân"
    if (a == b or a == c or b == c)
    and (a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a)
    else "Tam giác cân"
    if a == b or a == c or b == c
    else "Tam giác vuông"
    if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a
    else "Tam giác thường"
)

a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

print(phan_loai_tam_giac(a, b, c))