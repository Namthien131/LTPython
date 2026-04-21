s = input("Nhập chuỗi S: ")
vi_tri_not = s.find("not")
vi_tri_poor = s.find("poor")

if vi_tri_not != -1 and vi_tri_poor != -1 and vi_tri_not < vi_tri_poor:
    s = s[:vi_tri_not] + "good" + s[vi_tri_poor + 4:]

print("Chuỗi sau khi xử lý là:", s)