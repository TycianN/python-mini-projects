#importlar
import json
import os

#giriş mesajı
print("Hoşgeldiniz!")
skorlar_sozlugu={
     
}

#inputları alıcaz
while True:
    girilen_isim=input("İsim Giriniz(bitirmek için çıkış yazın): ")
    if girilen_isim=="çıkış":
            break
    else:
        try:
            girilen_skor=int(input("Skor Giriniz: "))
            skorlar_sozlugu[girilen_isim]=girilen_skor
        except ValueError:
            print("Lütfen Sayı Giriniz.")


# dosyayı oluşturucaz
if not os.path.exists("oyuncu_skorlari.json"):
     with open("oyuncu_skorlari.json","w",encoding="utf-8") as dosya:
        json.dump(skorlar_sozlugu,dosya,indent=4)
        print("Skorlar Başarıyla kaydedildi!")
else:
    print("Aynı isimde dosya bulunuyor: Oyuncu_Skorlari.json")
    delete_soru=input("Silmek İstermisiniz(e/h)?")
    if delete_soru=="e":
          os.remove("oyuncu_skorlari.json")
          if not os.path.exists("oyuncu_skorlari.json"):
            with open("oyuncu_skorlari.json","w",encoding="utf-8") as dosya:
                json.dump(skorlar_sozlugu,dosya,indent=4)
                print("Skorlar Başarıyla kaydedildi!")
    elif delete_soru=="h":
        print("işlem yapılmadı.")
    
     
            





    
    
