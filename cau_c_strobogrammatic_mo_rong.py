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


print("Cac so strobogrammatic mo rong < 1000000:")

for i in range(0, 1000000):
    if la_strobogrammatic_mo_rong(i):
        print(i, end=" ")