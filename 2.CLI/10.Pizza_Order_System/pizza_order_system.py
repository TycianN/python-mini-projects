#GİRİŞ MESAJI
print("Pizza Sipariş Sistemine Hoşgeldiniz! Lütfen Aşağıdaki Bilgileri Eksiksiz Doldurunuz.")

#SORULAR KISMI
boyut=input(f"Lütfen Pizza Boyutunu Seçiniz (S/M/L/XL): ").upper()
ekstra_sos=input(f"Lütfen Ekstra Sos Seçimi Yapınız (Evet/Hayır): ").capitalize()
ekstra_peynir=input(f"Lütfen Ekstra Peynir Seçimi Yapınız (Evet/Hayır): ").capitalize()
ucret=0
#BOYUT KONTROLÜ
if boyut=="S":
    ucret=+500
elif boyut=="M":
    ucret=+600
elif boyut=="L":
    ucret=+700
elif boyut=="XL":
    ucret=+800
else:
    print("Geçersiz Boyut Seçimi Yaptınız! Lütfen Tekrar Deneyiniz.")
#EKSTRA SOS KONTROLÜ
if ekstra_sos=="evet":
    ucret=+160
#EKSTRA PEYNİR KONTROLÜ
if ekstra_peynir=="evet":
    ucret=+200


#SONUÇ + ADRES KISMI
print(f"Toplam Ücretiniz: {ucret} TL'dir. Adresinize En Kısa Sürede Teslim Edilecektir. Lütfen Adres Bilgilerinizi Eksiksiz Doldurunuz.")
adres=input("Lütfen Adresinizi Giriniz: ")
print(f"Adresiniz: {adres}")
onay=input("adresinizi Onaylamak İçin Evet Düzenlemek İçin Hayır Yazınız: ")
if onay=="evet":
    print("Adresiniz Onaylanmıştır. Siparişiniz En Kısa Sürede Teslim Edilecektir. İyi Günler Dileriz!")
else:
    adres=input("Adresiniz Düzenlenmek Üzere Tekrar Girilmesi Gerekmektedir. Lütfen Adresinizi Tekrar Giriniz: ")
    onay2=input(f"Yeni Adresiniz: {adres} Onaylamak İçin Evet Düzenlemek İçin Hayır Yazınız: ")
if onay2=="evet":
    print("Adresiniz Onaylanmıştır. Siparişiniz En Kısa Sürede Teslim Edilecektir. İyi Günler Dileriz!")
else:
    print("Adresiniz Onaylanmadığı İçin Siparişiniz İptal Edilmiştir. Lütfen Tekrar Deneyiniz.")