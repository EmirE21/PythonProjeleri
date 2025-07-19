def olayı_bul(metin, desen):
    sayı = 0
    indeksler = []
    for i in range(len(metin) - len(desen) + 1):
        if metin[i:i + len(desen)] == desen:
            sayı += 1
            indeksler.append(i)
    if sayı > 0:
        return (True, sayı, indeksler)
    else:
        return (False, 0, [])

metin = input()
desen = input()
sonuç = olayı_bul(metin, desen)
print(sonuç)