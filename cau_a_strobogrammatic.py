

def la_strobogrammatic(n):
    doi = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

    s = str(n)
    kq = ""

    for c in reversed(s):
        if c not in doi:
            return False
        kq += doi[c]

    return kq == s


print("Cac so strobogrammatic < 1000000:")

for i in range(0, 1000000):
    if la_strobogrammatic(i):
        print(i, end=" ")