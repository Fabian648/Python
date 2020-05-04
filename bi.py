n = int(input("Gib eine Zahl an: "))

er = []
zw = []
i = 0

while n >0:
    i = int(n/2)
    zw.insert(0,i)
    i = n%2
    er.insert(0,i)
    n = zw[0]
print(er[0 :])