from collections import Counter

s1 = input("Nhập S1: ")
s2 = input("Nhập S2: ")

c1 = Counter(s1)
c2 = Counter(s2)

common = c1 & c2
print("Ký tự xuất hiện trong cả 2:", list(common.keys()))