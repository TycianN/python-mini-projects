# AD BİLGİSİ ALMA KISMI
ad=input("Lütfen adınızı Giriniz: ")

# SOYAD BİLGİSİ ALMA KISMI
soyad=input("Lütfen soyadınızı giriniz: ")

# UZUNLUĞUNU ALMA KISMI
ad_uzunluk=(len(ad))
soyad_uzunluk=(len(soyad))

# EKRANA YAZDIRMA KISMI
print(ad+" adının uzunluğu: "+str(ad_uzunluk))
print(soyad+" Soyadının Uzunluğu: "+str(soyad_uzunluk))

# GİZLİ KOD OLUŞTURMA VE EKRANA YAZMA KISMI
doğru_gizli_kod=ad[1:3]+soyad[3:6]+ str(ad_uzunluk) + str(soyad_uzunluk)
print("Gizli Kodunuz: "+doğru_gizli_kod)

# GİZLİ KODU DOĞRULAMA KISMI
while True:
    try:
        gizli_kod=input("Lütfen iletilen gizli kodu giriniz: ")
        if gizli_kod==doğru_gizli_kod:
            print("Giriş Başarılı Programı Kapatabilirsiniz!")
            break
        else:
            print("Giriş Hatalı Lütfen Tekrar Deneyiniz")
    except:
        print("Bir Hata Oluştu :(")



