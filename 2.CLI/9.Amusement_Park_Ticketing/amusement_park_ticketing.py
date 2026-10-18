#GİRİŞ MESAJI
print("Lunapark'a Hoşgeldiniz! Lütfen Aşağıdaki Bilgileri Eksiksiz Doldurunuz.")
boy=int(input("Lütfen Boyunuzu Cm Cinsinden Giriniz: "))

#ŞARTLAR KISMI
if boy>=120:
    print("Tebrikler! Lunapark'a Girebilirsiniz. İyi Eğlenceler Dileriz!")
    yas=int(input("Lütfen Yaşınızı Giriniz: "))
    if yas<12:
        ucret=50
        print(f"Ücret {ucret} TL'dir.")
    elif yas<18:
        ucret=100
        print(f"Ücret {ucret} TL'dir.")
    else:
        ucret=200
        print(f"Ücret {ucret} TL'dir.")
    foto=input("Fotoğraf Çekilmek İster Misiniz? (Evet/Hayır): ")
    if foto.lower()=="evet":
        ucret=ucret+20
        print(f"Toplam {ucret} TL Ücret Alınacaktır.")
    else:
        print("Fotoğraf Çekilmek İstenmediği İçin Ücret Alınmayacaktır.")
else:
    print("Üzgünüz, Boyunuz 120 Cm'den Kısa Olduğu İçin Lunapark'a Giremiyorsunuz!")
