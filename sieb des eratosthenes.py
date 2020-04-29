n = int(input("Gib das Ende eines Zahlenraums an: \n"))

def sieve(n):

    prim = []
    zah = list(range(2 , n))
    z = 2

    while z * z < n:
        for i in range(z,n,z):
            if i in zah:
                zah.remove(i)
        prim.append(z)
        z = zah[0]
    return prim + zah

print(sieve(n))