s = input("Nhập chuỗi S: ")
word = input("Nhập từ cần đếm: ")

s = s.lower()
word = word.lower()

s = s.replace(",", "")
s = s.replace(".", "")
s = s.replace("!", "")
s = s.replace("?", "")
s = s.replace(";", "")
s = s.replace(":", "")

ds_tu = s.split()

dem = 0
for tu in ds_tu:
    if tu == word:
        dem += 1

print("Số từ", word, "là", dem)