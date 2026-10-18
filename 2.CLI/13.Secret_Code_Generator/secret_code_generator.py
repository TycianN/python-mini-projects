#Başlık
Program_ad="Capitalize, Upper, Lower & Gizli Kod Oluşturma Programı"
Versiyon=1.2
print("*"*35)
print(Program_ad.upper(), f"Version :{Versiyon}")
print("*"*35)

# Bilgi Toplama Kısmı
İsim=input("İsminizi Giriniz: ")
Soyisim=input("Soyisminizi Giriniz: ")
Sehir=input("Yaşadığınız Şehri Giriniz: ")
Dogum_Yili=input("Doğum Yılınızı Giriniz: ")

# İnputları(Bilgileri) Farklı Biçimlerde Ekrana Yazdırma Kısmı

# Capitalize, Upper, Lower Kullanımı
print("İsminiz: ", İsim.capitalize())
print("İsminiz: ", İsim.upper())
print("İsminiz: ", İsim.lower())
print("*"*35)
print("soyisminiz: ", Soyisim.capitalize())
print("Soyisminiz: ", Soyisim.upper())
print("Soyisminiz: ", Soyisim.lower())
print("*"*35)
print("Yaşadığınız Şehir: ", Sehir.capitalize())
print("Yaşadığınız Şehir: ", Sehir.upper())
print("Yaşadğınız Şehir: ", Sehir.lower())
print("*"*35)
print("Doğum Yılınız: ", Dogum_Yili.capitalize())
print("Doğum Yılınız: ", Dogum_Yili.upper())
print("Doğum Yılınız: ", Dogum_Yili.lower())

# İnputtaki Farklı Karakterleri Alıp Ekrana Yazma Kısmı
print("*"*35)
print("İsminiz: ".upper())
print(İsim.capitalize())

print("*"*35)
print("Soyisminiz: ".upper())
print(Soyisim.capitalize())

print("*"*35)
print("Yaşadığınız Şehir: ".upper())
print(Sehir.capitalize())

print("*"*35)
print("Doğum Yılınız: ".upper())
print(Dogum_Yili.capitalize())

# Gizli Kod Oluşturma Kısmı
print("-"*35)
print("Gizli Kod: ".upper(),İsim[4:6] + Soyisim[1:3] + Sehir[4:6] + Dogum_Yili[2:4])
print("-"*35)

# Başarılı Mesajı
print("başarılı bir şekilde tamamlandı,".upper()+" "+"Lütfen Bilgilerinizi Kontrol Ettikten Sonra Kodu Kullanınız!")

#Kodu Kullanma Kısmı
dogru_kod=İsim[4:6] + Soyisim[1:3] + Sehir[4:6] + Dogum_Yili[2:4]
print("-"*35)
Toplam_Hak=3
giris_basarili=False
for deneme in range(3): # Toplam Hak
    kalan_hak = Toplam_Hak - deneme # hak matematiği
    print(f"Kalan Hakınız: {kalan_hak}") # hakları ekrana yazma
    girilen_kod = input("Lütfen Size İletilen Gizli Kodu Giriniz: ") # kodu girme
#Eğer girilen Kod doğruysa "BREAK" komutu ile kırıp kod başarılı yazısını yazdık.
    if girilen_kod == dogru_kod:
        print("Gizli kod doğru, lütfen devam ediniz!")
        giris_basarili = True
        break
# eğer kod yanlış ise ELSE komutu ile onu kontrol ettik yanlış ise döngüyse soktuk yukarıda ve gizli kod yanlış uyarısı verip tekrardan denettik eğer kalan hak toplam haktan az ise çok fazla deneme uyarısı verdik.
    else:
        print("Gizli Kod Yanlış, Lütfen Tekrar Deneyiniz!")
        print("*" * 35)
if not giris_basarili:
    print("Çok Fazla Yanlış Deneme, Daha Sonra Tekrar Dene!")