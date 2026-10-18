import random
import time

# ------------------------------
# 1. OYUNUN AÇILIŞ EKRANI
# ------------------------------

print("Sayı bilme oyununa hoş geldiniz!")
print("Lütfen oyuna başlamadan önce zorluk seçiniz.")
print("1. Kolay")
print("2. Zor")

# Zorluk seçimi geçerli olana kadar kullanıcıya sor.
while True:
    try:
        zorluk_secimi = int(input("Lütfen bir zorluk seç (1/2): "))

        if zorluk_secimi == 1:
            print("Kolay mod seçildi!")
            oyuncu_cani = 10
            ai_cani = 10
            break

        elif zorluk_secimi == 2:
            print("Zor mod seçildi!")
            oyuncu_cani = 5
            ai_cani = 5
            break

        else:
            print("Lütfen yalnızca 1 veya 2 seç.")

    except ValueError:
        print("Lütfen sayı gir.")

# ------------------------------
# 2. OYUN HAZIRLIĞI
# ------------------------------

time.sleep(1)
print("****************************")
print("Sayı seçiliyor...")
time.sleep(1)

# Gizli sayı yalnızca bir kere seçilir.
# Döngünün içinde olmadığı için her turda değişmez.
secilen_sayi = random.randint(1, 10)

print("Sayı seçildi!")
print("1 ile 10 arasında bir sayı tahmin et.")

# Başlangıç skorları
skor_tablosu_sen = 0
skor_tablosu_ai = 0

# ------------------------------
# 3. ANA OYUN DÖNGÜSÜ
# ------------------------------

while oyuncu_cani > 0 and ai_cani > 0:

    # Önce oyuncunun tahminini al.
    try:
        girilen_tahmin = int(input("Senin tahminin (1-10): "))

        # Aralık kontrolü: 1-10 dışındaki tahminler geçersiz.
        if girilen_tahmin < 1 or girilen_tahmin > 10:
            print("1 ile 10 arasında bir sayı girmelisin!")
            continue

    except ValueError:
        print("Lütfen geçerli bir tam sayı gir.")
        continue

    # AI da aynı gizli sayı için tahmin yapar.
    ai_girilen_sayi = random.randint(1, 10)
    print(f"AI'ın seçimi: {ai_girilen_sayi}")

    # ------------------------------
    # 4. TAHMİNLERİ DEĞERLENDİR
    # ------------------------------

    # Oyuncunun doğru tahmini
    if girilen_tahmin == secilen_sayi:
        print("Tebrikler, doğru tahmin ettin!")
        skor_tablosu_sen += 1
        break

    # AI'ın doğru tahmini
    elif ai_girilen_sayi == secilen_sayi:
        print("AI doğru tahmin etti!")
        skor_tablosu_ai += 1
        break

    # İkisi de bilemediyse
    else:
        print("İkiniz de bilemediniz!")

        # Her yanlış tahmin edenin canını azalt.
        oyuncu_cani -= 1
        ai_cani -= 1

        print(f"Senin canın: {oyuncu_cani}")
        print(f"AI'ın canı: {ai_cani}")

        print(f"Sen: {skor_tablosu_sen} | AI: {skor_tablosu_ai}")
        print("Aynı sayı için tekrar deneyin!")

# ------------------------------
# 5. OYUN SONU
# ------------------------------

print("\n****************************")
print("OYUN BİTTİ!")
print(f"Senin skorun: {skor_tablosu_sen}")
print(f"AI'ın skoru: {skor_tablosu_ai}")

if skor_tablosu_sen > skor_tablosu_ai:
    print("Oyunu sen kazandın! 🎉")

elif skor_tablosu_ai > skor_tablosu_sen:
    print("AI kazandı! 🤖")

else:
    print("Oyun berabere bitti!")