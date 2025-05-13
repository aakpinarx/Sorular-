fiyatlar = [104.25, 79.09, 42.75, "KırkBeş", 24.25]

toplam = 0
for i in fiyatlar:
    try:
        toplam += float(i)
    except:
        print("Hata: Geçersiz fiyat: ", i)
        
print("Toplam Fiyat:", toplam)
