def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = []
while True:
    n = int(input("Nhập số: "))
    numbers.append(n)
    if input("Tiếp? (Y/N): ").lower() == 'n':
        break

primes = [x for x in numbers if is_prime(x)]
print("Số nguyên tố:", primes)