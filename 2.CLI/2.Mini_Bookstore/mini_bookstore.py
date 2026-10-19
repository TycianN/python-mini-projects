#-------------------------------------------------------
#                       v1.2.0 notes
# you can now choose how much pages you want to read.
# added colours to the terminal page.
# added a few comment lines for more opacity.
#-------------------------------------------------------

# importlar
from colorama import Back,Fore,Style

#Giriş
print(Fore.BLUE+"Kütüphaneye hoşgeldiniz!")

#class ve def ler
class Kitap:
    def __init__(self,kitap_adi,sayfa_sayisi,yazar):
        print("kitaplar İnceleniyor Lütfen Bekleyiniz...")
        self.kitap_adi=kitap_adi
        self.sayfa_sayisi=sayfa_sayisi
        self.yazar=yazar
        self.okunan_sayfa=0
        self.kalan_sayfa=0
    def oku(self,miktar):
        self.okunan_sayfa+=miktar  
        self.kalan_sayfa=self.sayfa_sayisi-miktar  
    def oku_bilgi_ver(self):
        print(f"{self.kitap_adi}; {self.sayfa_sayisi} sayfaydı, {self.okunan_sayfa} Sayfa Okundu, {self.kalan_sayfa} Sayfa Kaldı")
    def bilgi_ver(self):
        print(f"Seçilen Kitap; \nKitap Adı: {self.kitap_adi}, Sayfa Sayısı: {self.sayfa_sayisi}, Yazar: {self.yazar}")

#kitapları özelleştirme
kitap1=Kitap("The Echoes Of Obsidian",384,"TycianN")
kitap2=Kitap("Unwritten Laws Of Time",245,"TycianN")
print(f"1. Kitap; \nKitabın Adı: {kitap1.kitap_adi}")
print(f"2. Kitap; \nKitabın Adı: {kitap2.kitap_adi}")

# input(okuma kısmı)
while True:
    try:
        kitap_soru=int(input("hangi kitabı okumak istersin(1/2): "))
        if kitap_soru==1:
            kitap1.bilgi_ver()
            sayfa_soru1=int(input("Kaç Sayfa Okumak İstersin: "))
            kitap1.oku(sayfa_soru1)
            kitap1.oku_bilgi_ver()
            
        elif kitap_soru==2: # daha fazla kitap ekleyebilmek için elif kullanıldı normalde else de kullanılabilirdi.
            kitap2.bilgi_ver()
            sayfa_soru2=int(input("Kaç Sayfa Okumak İstersin: "))
            kitap2.oku(sayfa_soru2)
            kitap2.oku_bilgi_ver()
            
        devam_mi=input("Başka Bir Kitap Okumak İstermisiniz(e/h):")
        if devam_mi=="e":
            print("Oluşturuluyor... Şuanda Kullanılamaz.")
            break
        else:
            print("Bu Kadar Okuma Yeterli Olmalı... Görüşmek Üzere.")
            break
    except ValueError:
        print("Lütfen Sayı Giriniz.")
    
