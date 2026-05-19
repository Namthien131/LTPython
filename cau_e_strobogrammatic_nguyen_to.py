
import math

def la_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def strobogrammatic(n):
    doi = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6'
    }

    s = str(n)
    kq = ""

    for c in reversed(s):
        if c not in doi:
            return -1

        kq += doi[c]

    return int(kq)


def la_strobogrammatic(n):
    return strobogrammatic(n) == n


print("Cac so thoa dieu kien:")

for i in range(0, 1000000):

    if not la_strobogrammatic(i) and not la_nguyen_to(i):

        so_dao = strobogrammatic(i)

        if so_dao != -1 and la_nguyen_to(so_dao):
            print(i, end=" ")