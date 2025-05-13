sozluk = {
    "elma": "Apple",
    "ananas": "Pineapple",
    "muz": "Banana"
}

anahtar = input("Bir meyve adı giriniz: ")

if anahtar in sozluk:
    print(sozluk[anahtar])
else:
    print("Anahtar bulunamadı!")

