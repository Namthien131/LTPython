numbers = []
while True:
    n = int(input("Nhập số: "))
    numbers.append(n)
    if input("Tiếp? (Y/N): ").lower() == 'n':
        break

neg = [x for x in numbers if x < 0]
pos = [x for x in numbers if x > 0]

if neg:
    print("TBC âm:", sum(neg)/len(neg))
else:
    print("Không có số âm")

if pos:
    print("TBC dương:", sum(pos)/len(pos))
else:
    print("Không có số dương")