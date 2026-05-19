
import math

def la_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def la_strobogrammatic_mo_rong(n):
    doi = {
        '0': '0',
        '1': '1',
        '2': '2',
        '5': '5',
        '6': '9',
        '8': '8',
        '9': '6'
    }

    s = str(n)
    kq = ""

    for c in reversed(s):
        if c not in doi:
            return False
        kq += doi[c]

    return kq == s


print("Cac so nguyen to strobogrammatic mo rong < 1000000:")

for i in range(0, 1000000):
    if la_strobogrammatic_mo_rong(i) and la_nguyen_to(i):
        print(i, end=" ")