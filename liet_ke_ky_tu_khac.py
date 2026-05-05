s1 = input("Nhập S1: ")
s2 = input("Nhập S2: ")

set1 = set(s1)
set2 = set(s2)

only_s1 = set1 - set2
only_s2 = set2 - set1

print("Ký tự có trong S1 nhưng không có trong S2:", list(only_s1))
print("Ký tự có trong S2 nhưng không có trong S1:", list(only_s2))