s1 = input("Nhập S1: ")
s2 = input("Nhập S2: ")

set1 = set(s1)
set2 = set(s2)

only_s1 = set1 - set2
only_s2 = set2 - set1

print("Số ký tự chỉ có trong S1:", len(only_s1))
print("Số ký tự chỉ có trong S2:", len(only_s2))