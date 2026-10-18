import random

while True:
    # 1. Kullanıcıdan her turda YENİ tahmin al ve int'e çevir
    soru = int(input("\nYazı Mı(0)? Tura Mı(1)?: "))
    
    # 2. Her turda YENİ rastgele sayı üret
    rastgele = random.randint(0, 1)
    
    print(f"Gelen sonuç: {rastgele}")
    
    # 3. Karşılaştır
    if soru == rastgele:
        print("Doğru tahmin!")
    else:
        print("Yanlış tahmin tekrar deneyebilirsin.")
        
    # 4. Çıkış kontrolü
    devam = input("Tekrar oynamak ister misin? (e/h): ")
    if devam.lower() != "e":
        print("Oyun bitti!")
        break



