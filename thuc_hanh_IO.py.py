import zlib
import os

with open("fileName.txt", "w", encoding="utf-8") as f:
    f.write("Thuyền và biển\nChỉ có thuyền mới hiểu\nBiển mênh mông nhường nào\n...\n")

print("Đã tạo fileName.txt")
print("Kích thước file gốc:", os.path.getsize("fileName.txt"), "bytes")

with open("fileName.txt", "rb") as f:
    du_lieu_goc = f.read()

du_lieu_nen = zlib.compress(du_lieu_goc)

with open("compressed.bin", "wb") as f:
    f.write(du_lieu_nen)

print("Đã nén file thành compressed.bin")
print("Kích thước file nén:", os.path.getsize("compressed.bin"), "bytes")

with open("compressed.bin", "rb") as f:
    du_lieu_nen2 = f.read()

du_lieu_goc2 = zlib.decompress(du_lieu_nen2)

with open("decompressed.txt", "wb") as f:
    f.write(du_lieu_goc2)

print("Đã giải nén ra decompressed.txt")
print("Xong!")