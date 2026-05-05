numbers = []
while True:
    n = int(input("Nhập số: "))
    numbers.append(n)
    if input("Tiếp? (Y/N): ").lower() == 'n':
        break

is_sorted = True
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i+1]:
        is_sorted = False
        break

print("Tăng dần:", is_sorted)