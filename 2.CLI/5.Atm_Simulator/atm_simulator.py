#V2 Plan Notları
# kullanıcı kayıt eklenecek,  kart no(16 hane) ve cvv(3 hane) tanımlanacak. 
# kayıt olmadan menüye ulaşamayacak.
bakiye=0
print("1-Bakiye Sorgula")
print("2-Para Yatır")
print("3-Para Çek")
print("4-Çıkış")
while True:
    try:
        Girilen_istek=int(input("Lütfen Bir İşlem Seçiniz: "))
        #BAKİYE SORGULAMA KISMI
        if Girilen_istek==1:
             print (f"Bakiyeniz {bakiye} TL Dir.")
            #PARA YATIRMA KISMI
        elif Girilen_istek==2:
            print("Para Yatırma Menüsü Açılıyor...")
            print("1-Dolar(Bakımda)")
            print("2-TL")
            print("3-GBP(Bakımda)")
            py_istek=int(input("Devam Etmek İstediğiniz Kuru Seçiniz: "))
            if py_istek==1:
                print("Dolar Olarak Devam Edilemiyor.")
            elif py_istek==3:
                print("GBP Olarak Devam Edilemiyor.")
            elif py_istek==2:
                print("TL Olarak Devam Ediliyor.")
                while True:
                    py_miktar=int(input("Kaç TL Yatırmak İstersiniz:"))
                    if py_miktar>=100:
                        bakiye+=py_miktar
                        print("İşlem Başarıyla Gerçekleşti!")
                        break
                    else:
                        print("Çok Küçük Miktar.")
                print("1-Bakiye Sorgula")
                print("2-Çıkış")
                py_siradaki_islem=int(input("Ne İle Devam Etmek İstersiniz: "))
                if py_siradaki_islem==1:
                    print(f"Bakiyeniz {bakiye} TL Dir, Ana Menüye Dönülüyor.")
                elif py_siradaki_islem==2:
                    print("Çıkış Sağlandı. Görüşmek Üzere...")
                    break  
             #PARA ÇEKME KISMI
        elif Girilen_istek==3:
            if bakiye==0:
                print("Bakiyeniz 0 TL olduğu için para çekemezsiniz.")
                continue
            print("Para Çekme Menüsü Açılıyor...") 
            print (f"Bakiyeniz {bakiye} TL dir.")  
            while True: 
                pc_istek=int(input(f"Kaç TL Çekmek İstersiniz? (Max. {bakiye} TL): "))
                if pc_istek <= 0:
                    print("Lütfen 0'dan büyük bir miktar giriniz.")
                elif pc_istek>bakiye:
                    print("Bakiye yetersiz Lütfen Tekrar Dene.")
                else:
                    bakiye-=pc_istek
                    print("İşlem Başarılı. Ana Menüye Dönülüyor...")

                    break
        elif Girilen_istek==4:
            print("Program Kapatılıyor...")
            break
        else:
            print("Lütfen 1-4 Arası Bir Seçim Yapınız.")
    except ValueError:
        print("Lütfen Sayı Giriniz!")
        
    


