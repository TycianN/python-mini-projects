print("Kütüphaneye hoşgeldiniz!")
class Kitap:
    def __init__(self,kitap_adi,sayfa_sayisi,yazar):
        print("kitaplar İnceleniyor Lütfen Bekleyiniz...")
        self.kitap_adi=kitap_adi
        self.sayfa_sayisi=sayfa_sayisi
        self.yazar=yazar
kitap1=Kitap("The Echoes Of Obsidian",384,"TycianN")
kitap2=Kitap("Unwritten Laws Of Time",245,"TycianN")
print("1. kitap;")
print(f"Kitabın Adı: {kitap1.kitap_adi} \n Kitabın Sayfa Sayısı: {kitap1.sayfa_sayisi} \n Kitabın Yazarı: {kitap1.yazar}")
print("2. kitap;")
print(f"Kitabın Adı: {kitap2.kitap_adi} \n Kitabın Sayfa Sayısı: {kitap2.sayfa_sayisi} \n Kitabın Yazarı: {kitap2.yazar}")


