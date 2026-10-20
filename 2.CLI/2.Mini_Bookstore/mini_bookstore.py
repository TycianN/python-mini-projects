#-------------------------------------------------------
#                       v1.2.0 notes
# you can now choose how many pages you want to read.
# added colors to the terminal page.
# added a few comment lines for better readability.
# will be updated frequently like all of the other GUI and CLI projects.
#                       v1.3.0 notes
# small optimizations, added audiobook option using --child class.
#                       v1.3.1 plan
# sort out "continue to read" option, Maybe add a few more books...
#-------------------------------------------------------
# importlar
from colorama import Back,Fore,Style

# Giriş
print(Fore.BLUE+"Kütüphaneye hoşgeldiniz!")

# class ve def ler
class Kitap: # main class
    def __init__(self,kitap_adi,sayfa_sayisi,yazar):
        print("kitaplar İnceleniyor, Lütfen Bekleyiniz...")
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

class Sesli_kitap(Kitap): # childclass
    def __init__(self,kitap_adi,sayfa_sayisi,yazar,seslendiren):
        super().__init__(kitap_adi,sayfa_sayisi,yazar)
        self.seslendiren=seslendiren
    def dinle_bilgiver(self):
        print(f"{self.kitap_adi}; {self.sayfa_sayisi} sayfaydı, Seslendirmen -{self.seslendiren}- Tarafından {self.okunan_sayfa} Sayfa Dinlendi, {self.kalan_sayfa} Sayfa Kaldı")



# kitapları özelleştirme
# Okunan Kitaplar
kitap1=Kitap("The Echoes Of Obsidian",384,"TycianN")
kitap2=Kitap("Unwritten Laws Of Time",245,"TycianN")

# Sesli Kitaplar
seskitap1=Sesli_kitap("The Echoes Of Obsidian",384,"TycianN","Taycan")
seskitap2=Sesli_kitap("Unwritten Laws Of Time",245,"TycianN","Taycan")

# seçim sorusunu sormadan önce kitapları gösteriyoruz
print(f"1. Kitap; \nKitabın Adı: {kitap1.kitap_adi}")
print(f"2. Kitap; \nKitabın Adı: {kitap2.kitap_adi}")

# inputlar(okuma ve dinleme kısmı)
while True:
    try:
        kitap_soru=int(input("hangi kitabı seçmek istersin(1/2): "))
        if kitap_soru==1:
            kitap1.bilgi_ver()
            seslidinle_soru1=input("Sesli mi dinlemek istersin yoksa okumak mı istersin(s/o): ")
            if seslidinle_soru1=="o":
                sayfa_soru1=int(input("Kaç Sayfa Okumak İstersin: "))
                kitap1.oku(sayfa_soru1)
                kitap1.oku_bilgi_ver()
            else:
                sayfa_soru11=int(input("Kaç Sayfa dinlemek İstersin: "))
                seskitap1.oku(sayfa_soru11)
                seskitap1.dinle_bilgiver()

            
        elif kitap_soru==2: # daha fazla kitap ekleyebilmek için elif kullanıldı normalde else de kullanılabilirdi.
            kitap2.bilgi_ver()
            seslidinle_soru2=input("Sesli mi dinlemek istersin yoksa okumak mı istersin(s/o): ")
            if seslidinle_soru2=="o":
                sayfa_soru2=int(input("Kaç Sayfa Okumak İstersin: "))
                kitap2.oku(sayfa_soru2)
                kitap2.oku_bilgi_ver()
            else:
                sayfa_soru22=int(input("Kaç Sayfa Okumak İstersin: "))
                seskitap2.oku(sayfa_soru22)
                seskitap2.dinle_bilgiver()
            
        # devam mı kısmı(yazılıyor, tamamlanmadığı için break ile döngü kırılıyor.)    
        devam_mi=input("Başka Bir Kitap Okumak İstermisiniz(e/h):")
        if devam_mi=="e":
            print("Oluşturuluyor... Şuanda Kullanılamaz.")
            break
        else:
            print("Bu Kadar Okuma Yeterli Olmalı... Görüşmek Üzere.")
            break
    except ValueError:
        print("Lütfen Sayı Giriniz.")
    
