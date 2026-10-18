# Fiyat Listesi Belirleme
fiyatlar=[1000, 10000, 15000, 20000, 25000, 30000]

# Max Bütçeyi Alma (Sayısal karşılaştırma yapacağımız için int 
max_butce=int(input("Lütfen Maksimum Gecelik Bütcenizi Giriniz(TL): "))

# # Ekrana dinamik değişken basmak için f-string kullanıldı
print(f"{max_butce} TL Altındaki Uygun Oteller")

# Sayaçları döngüden önce sıfırlıyoruz
uygun_otel_sayisi=0
toplam_fiyat=0

#Döngü kısmı
for i in fiyatlar:  # Fiyatlar listesindeki her bir fiyatı sırayla 'i' değişkenine ata
    if i>max_butce:  # Eğer fiyat kullanıcının bütçesini aşıyorsa
        continue  # Alt satırlara inme, bu oteli ATLA ve döngünün başına dön!

    # Bütçeyi aşmayan (uygun) oteller için bu satırlar çalışır:
    print(f"-{i} TL") # analiz sonucunu ekrana yazdık
    uygun_otel_sayisi+=1 # Bulunan uygun otel adedini 1 artır
    toplam_fiyat+=i # Uygun otelin gerçek fiyatını toplam kasasına ekle

print("-" * 30)
print(f"{uygun_otel_sayisi} Uygun Otel Bulundu!") 

# Sıfıra bölme hatasını (ZeroDivisionError) engellemek için kontrol
if uygun_otel_sayisi>0: 
    ortalama=toplam_fiyat/uygun_otel_sayisi 
    print(f"Uygun Otellerin Ortalama Fiyatı: {round(ortalama, 2)} TL") 
else: 
    print("Bütçenize uygun otel bulunamadığı için ortalama hesaplanamadı.") 

sayac=0
while sayac<10:
    # print(f"sayacımız {sayac}")
    # sayac+=1
    pass # işlemleri şimdilik pas geç 
print("merhaba dünya")


# Sayı Ortalaması Hesaplayıcı
toplam=0
sayac=0
Sayı=0
print("Sayıları Giriniz: (Ortalamayı Hesaplamak için -1 yazınız)")
Sayı=float(input("Sayı Giriniz: "))
# not_girişi=float(input("Not="))
# while not_girişi!=-1:
# VEYA
while(Sayı:=float(input("Not:")))!=-1:
    toplam+=Sayı
    sayac+=1
if sayac>0:
    print(f"Ortalama: {toplam/sayac}")
else:
    print("Hiç Sayı Girilmemiştir.")



# Dosya Tarama Ve Bulma
import os
import time
dosya_yolu="Rapor.docx"
timeout=30
baslangic=time.time()
print("Dosya Bekleniyor...")
while not os.path.exists(dosya_yolu):
    gecen_sure=time.time()-baslangic
    if gecen_sure>30:
        print("Zaman Aşımı! Dosya Bulunamadı")
        break
    print(f"Bekleniyor... {int(gecen_sure)} Saniye")
    time.sleep(2)
else:
    print("Dosya Başarıyla Tespit Edildi, İşlemlere Başlanıyor")






