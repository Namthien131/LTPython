numbers = []
while True:
    n = int(input("Nhập số: "))
    numbers.append(n)
    if input("Tiếp? (Y/N): ").lower() == 'n':
        break

print("Max:", max(numbers))
print("Min:", min(numbers))