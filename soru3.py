liste = ["elma", "armut", "muz", "çilek", "kiraz"]

try:
    i = int(input("İndeks girin: "))
    print(liste[i])
except (ValueError, IndexError):
    print("Geçersiz indeks!")
