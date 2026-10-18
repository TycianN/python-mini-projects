from colorama import Fore,Style,Back # ders 15 update
eleman_maaslari = {
    "id_101": {
        "isim": "Ahmet",
        "maas": 0
    },
    "id_102": {
        "isim": "Mehmet",
        "maas": 0
    },
    "id_103": {
        "isim": "Selman",
        "maas": 0
    },
    "id_104": {
        "isim": "Erkan",
        "maas": 0
    }
}

# İsimleri alıyoruz
id101_isim = eleman_maaslari["id_101"]["isim"]
id102_isim = eleman_maaslari["id_102"]["isim"]
id103_isim = eleman_maaslari["id_103"]["isim"]
id104_isim = eleman_maaslari["id_104"]["isim"]

# Kullanıcıdan maaşları alıp sözlüğü güncelliyoruz (Update: Eşittir kaldırıldı!)
yeni_maas101 = int(input(f"{id101_isim}'in Maaşını Belirleyiniz: "))
eleman_maaslari["id_101"]["maas"] = yeni_maas101

yeni_maas102 = int(input(f"{id102_isim}'in Maaşını Belirleyiniz: "))
eleman_maaslari["id_102"]["maas"] = yeni_maas102

yeni_maas103 = int(input(f"{id103_isim}'in Maaşını Belirleyiniz: "))
eleman_maaslari["id_103"]["maas"] = yeni_maas103

yeni_maas104 = int(input(f"{id104_isim}'in Maaşını Belirleyiniz: "))
eleman_maaslari["id_104"]["maas"] = yeni_maas104

total_maaslar = yeni_maas101 + yeni_maas102 + yeni_maas103 + yeni_maas104
print(f"\nTotal Aylık Maaşlar: {total_maaslar}")

# Güncel maaşları doğrudan sözlükten çekerek yazdırıyoruz:
# id101
print("-------------------")
print(f"İsim: {id101_isim}")
print(f"Maaş: {eleman_maaslari['id_101']['maas']}")

# id102
print("-------------------")
print(f"İsim: {id102_isim}")
print(f"Maaş: {eleman_maaslari['id_102']['maas']}")

# id103
print("-------------------")
print(f"İsim: {id103_isim}")
print(f"Maaş: {eleman_maaslari['id_103']['maas']}")

# id104
print("-------------------")
print(f"İsim: {id104_isim}")
print(f"Maaş: {eleman_maaslari['id_104']['maas']}")

print(Fore.BLUE+Back.GREEN+Style.BRIGHT+"50.000 Den Fazla Ödenecek Zararlar:")

#zararlıları ölçüyoruz
zarar_listesi = []
for emp_id, bilgiler in eleman_maaslari.items():
    if bilgiler["maas"] > 50000:
        zarar_listesi.append(bilgiler["isim"])

if zarar_listesi:
    for isim in zarar_listesi:
        print("-------------------")
        print(isim)
else:
    print(Fore.GREEN+Back.RED+"50.000 TL nin üstünde maaş alan eleman yoktur. Yine şanslısın :)")