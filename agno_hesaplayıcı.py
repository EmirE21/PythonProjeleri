def agno_hesaplama(ders_ismi_liste, ders_kredi_liste, ders_harf_notu_liste):
    # Harf notları ve karşılık gelen sayısal değerler.
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
    akts = 0.0
    toplam_ortalama = 0.0
    # Üç ayrı liste bir araya getirilir ve isim, kredi, harf_notu formatında tekrar düzenlenir.
    for isim, kredi, harf_notu in zip(ders_ismi_liste, ders_kredi_liste, ders_harf_notu_liste):
        # Girilen harf notu doğru değilse uyarı verilir.
        if harf_notu not in harf_notu_sözlük:
            print(f"Uyarı: Lütfen harf notlarını küçük harflerle girdiğinizden emin olun.")
            return
        # AGNO hesabı için gerekli hesaplamalar yapılır.
        akts += kredi
        toplam_ortalama += harf_notu_sözlük[harf_notu] * kredi
    agno_değeri = toplam_ortalama / akts
    return agno_değeri
# Kullanıcıdan ders bilgileri alınır ve koşul sağlanırsa bilgiler kendi aralarında listelenir.
ders_bilgisi_girdi = input("Lütfen ders bilgilerinizi giriniz (örn: matematik 4 aa fizik 3 bb kimya 2 cc): ")
ders_bilgisi_liste = ders_bilgisi_girdi.split()
if len(ders_bilgisi_liste) % 3 != 0:
    print("Uyarı: Lütfen her ders için isim, kredi ve harf notu sırasına göre bilgileri tekrar giriniz.")
else:
    ders_ismi_liste = ders_bilgisi_liste[0:len(ders_bilgisi_liste):3]
    ders_kredi_liste = [int(kredi) for kredi in ders_bilgisi_liste[1:len(ders_bilgisi_liste):3]]
    ders_harf_notu_liste = ders_bilgisi_liste[2:len(ders_bilgisi_liste):3]
    sonuc = agno_hesaplama(ders_ismi_liste, ders_kredi_liste, ders_harf_notu_liste)
    print(f"AGNO: {sonuc}")