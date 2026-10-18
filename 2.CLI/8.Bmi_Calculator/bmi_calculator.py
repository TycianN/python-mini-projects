# BİLGİ TOPLAMA KISMI
Ad=input("Lütfen Adınızı Giriniz: ")
Soyad=input("Lütfen Soyadınızı Giriniz: ")
Dogum_Yili=int(input("Lütfen Doğum Yılınızı Giriniz: "))
Boy=float(input("Lütfen Boyunuzu Giriniz: "))
Kilo=float(input("Lütfen Kilonuzu Giriniz: "))

# İSİM FORMATLAMA KISMI
Ad=(Ad.capitalize())
Soyad=(Soyad.capitalize())
Ad_Uzunluk=len(Ad)
Soyad_Uzunluk=len(Soyad)
Ad_Soyad=((Ad_Uzunluk) + (Soyad_Uzunluk))

# YAŞ VE DOĞUM YILI ANALİZİ KISMI
Yas=2026-Dogum_Yili
Dekad=(Yas // 10)

# VÜCUT KİTLE İNDEKSİ HESAPLAMA KISMI
VKI=Kilo/Boy**2

# İDEAL KİLO HESAPLAMA KISMI
İdeal_Kilo=22*Boy**2

# KİLO FARKI HESAPLAMA KISMI
Kilo_Farki=Kilo-İdeal_Kilo

# RAPORLAMA KISMI
print("="*45)
print(f"Adınız Ve Soyadınız: {Ad} {Soyad}")
print("-"*30)
print(f"Gizli Danışan Kodunuz: {Ad[0:2].upper()}{Soyad[-2:].lower()}{Ad_Soyad}")
print("-"*30)
print(f"Yaşınız: {Yas}")
print("-"*30)
print(f"{Dekad} Dekaddır Dünyadasınız.")
print("-"*30)
print("Doğum Yılı Çift Mi Tek Mi?: "+str(Dogum_Yili % 2))
print("-"*30)
print(f"Vücut Kitle İndeksiniz: {VKI:.2f}")
print("-"*30)
print(f"İdeal Kilonuz: {İdeal_Kilo:.2f} Kg")
print("-"*30)
print(f"İdeal Kilonuza {Kilo_Farki:.2f} Kg Uzaktasınız!")
print("="*45)








