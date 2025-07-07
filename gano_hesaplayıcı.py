def gano_hesaplama():
    harf_notu_sözlük = {
        "aa": 4.0,
        "ba": 3.5,
        "bb": 3.0,
        "cb": 2.5,
        "cc": 2.0,
        "dc": 1.5,
        "dd": 1.0,
        "fd": 0.5,
        "ff": 0.0
    }
    orijin = 0.0
    for i in range(len(harf_notu_liste)):
        harf_notu = harf_notu_liste[i]
        if harf_notu in harf_notu_sözlük:
            orijin += harf_notu_sözlük[harf_notu]
    return orijin / len(harf_notu_liste)

harf_notu_girdi = input("Lütfen harf notlarınızı küçük harflerle giriniz: ")
harf_notu_liste = harf_notu_girdi.split()
sonuc = gano_hesaplama()
print(f"GANO: {sonuc}")