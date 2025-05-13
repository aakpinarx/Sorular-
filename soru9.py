while True:
    try:
        yas = int(input("Yaşınızı girin: "))
        if yas < 0:
            print("Yaş negatif olamaz!")
        else:
            break
    except ValueError:
        print("Lütfen sayısal bir değer girin.")

print("Girilen yaş:", yas)
