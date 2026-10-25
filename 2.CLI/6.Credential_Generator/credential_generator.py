#importlar
import random

# --- 1. Program Başlığı ---
program_ad = "Akıllı Karşılama ve Kimlik Oluşturucu"
versiyon = 1.0

print("-" * 30)
print(f"{program_ad} v {versiyon}")
print("-" * 30)

# --- 2. Bilgi Toplama Kısmı ---
ad = input("Lütfen Adınızı Giriniz: ")
soyad = input("Lütfen Soyadınızı Giriniz: ")
sehir = input("Lütfen Yaşadığınız Şehri Giriniz: ")
dogum_yili = input("Lütfen Doğum Yılınızı Giriniz: ")

# --- 3. İsim ve Metin Manipülasyonları ---
tam_ad = ad + " " + soyad
buyuk_ad = tam_ad.upper()
kucuk_sehir = sehir.lower()
bas_harf_soyad = soyad.capitalize()

# --- 4. Kullanıcı Özeti ---
print("-" * 10, "Kullanıcı Özeti".upper(), "-" * 10)
mesaj = f"Merhaba {ad.capitalize()}!\n{sehir.upper()} Şehrinde Yaşadığını Öğrendim."
print(mesaj)

# --- 5. Şifre ve Kullanıcı Adı Oluşturma (Dilimleme + Metotlar) ---
# Kural:
# - Adın küçük ilk 2 harfi
# - Soyadın büyük son 2 harfi
# - Doğum yılı
# - Özel karakter: '!,?,&,'
ozel_karakter_secici = random.chose["!","?","&"]
sifre_onerisi = ad[:2].lower() + soyad[-2:].upper() + dogum_yili + ozel_karakter_secici
kullanici_adi = f"{ad.lower()}_{dogum_yili}"

print("-" * 30)
print(f"Sistem için önerilen güvenli şifreniz: {sifre_onerisi}")
print(f"Kullanıcı adınız: {kullanici_adi}")
print("-" * 30)
print("Program başarıyla tamamlandı.")