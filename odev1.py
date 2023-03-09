# Soru1: Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.

# String veri tipi: Metinsel veri tipleridir. Tirnak icinde yazilir.
yazi1 = "kodlama.io birinci gun ders odevi"
print(yazi1)

print("         ")
print("*****************************************************************************************************")
print("         ")

# Boolean veri tipi. Ciktisi dogru ise True, yanlis ise False olarak dondurur.
sayi1 = 443
sayi2 = 344
print(bool(sayi1 == sayi2))

print("         ")
print("*****************************************************************************************************")
print("         ")

# Sayisal veri tipleri: int, float, complex
# int: Tam sayilar
# float: Ondalikli sayilar
# complex: Karmasik sayilar

sayi3 = 653
print(sayi3, type(sayi3), "Sayi 3 tam sayidir.")

sayi4 = 67.4321
print(sayi4, type(sayi4), "Sayi 4 ondalikli sayidir.")

sayi5 = 4.5j
print(sayi5, type(sayi5), "Sayi 5 bir karmasik sayidir.")

print("         ")
print("*****************************************************************************************************")
print("         ")

# Listeler. Burada farkli olarak koseli parantez kullanilir.

liste1 = ["Apple MBP", "Asus VivoBook", "Samsung S23", 4567, 6643.3]
liste2 = ["MacOS", "Windows", "Android"]
print(liste1)
print(liste1[0]) #listedeki ilk ogeyi yazdirir
print(liste1[1:3]) #ikinci ve ucuncu ogeyi yazdirir
print(liste1[2:]) #ucuncu ogeden sonrasini yazar
print(liste2 * 2) #listeyi 2 kere yazar
print(liste1 + liste2) #Iki listeyi birlestirir
print(type(liste1), "Liste1 bir listedir")
print(type(liste2), "Liste2 bir listedir")

print("         ")
print("*****************************************************************************************************")
print("         ")

#Tuples. Listeye gore farki sadece okunabilir (read only) olmasi ve yazarken koseli parantez yerine normal parantez kullanilmasidir.
#Burada mevcut ogelerin sayisi arttirilamaz veya guncellenemez.

tuple1 = ("Ayse", "Fatma", "Hayriye", 8765, 842.2357)
tuple2 = ("Kedi", "Kopek", "Kus")
print(tuple1)
print(tuple1[0]) #listedeki ilk ogeyi yazdirir
print(tuple1[1:3]) #ikinci ve ucuncu ogeyi yazdirir
print(tuple1[2:]) #ucuncu ogeden sonrasini yazar
print(tuple2 * 2) #listeyi 2 kere yazar
print(tuple1 + tuple2) #Iki listeyi birlestirir
print(type(tuple1), "Tuple1 bir tupledir")
print(type(tuple2), "Tuple2 bir tupledir")

print("         ")
print("*****************************************************************************************************")
print("         ")

#Range. Sifirdan baslayip belirli bir sayiya kadar artan bir sayi dizisini dondurur.

for i in range(11):
    print(i)

print("         ")
print("*****************************************************************************************************")
print("         ")

#Sozluk (dictionary). Veriler anahtar ve karsilarinda yer alan degerler seklinde tutulur. Liste ve Tuple'dan farki olusturulurken suslu parantez kullanilir.

dict1 = {"isim": "Ceren", "dogumTarihi": 1988, "meslek": "Akademisyen"}
print(dict1)
print(dict1["dogumTarihi"]) #dogumtarihindeki degeri yazdirir
print(dict1.keys()) #tum anahtarlari yazdirir
print(dict1.values()) #tum degerleri yazdirir
print(type(dict1), "dict1 bir sozluktur")

print("         ")
print("*****************************************************************************************************")
print("         ")

#Kumeler. Set, Frozenset. Set; liste, sozluk, tuples veri tiplerinin birlikte kullanilarak olusturulan kumeler.
#Frozensette ise tek fark kume icinde degisiklik yapilamamasidir. Burada da sozlukte oldugu gibi suslu parantez kullanilir.

kume1 = set(("Adidas", "Nike", "Puma"))
print(kume1)
print(type(kume1), "kume1 bir kumedir")

kume2 = set(liste1)
print(kume2)
print(type(kume2), "kume2 bir kumedir")

kume3 = set(tuple1)
print(kume3)
print(type(kume3), "kume3 bir kumedir")

kume4 = set(dict1)
print(kume4)
print(type(kume4), "kume4 bir kumedir")

print("         ")
print("*****************************************************************************************************")
print("         ")

#Soru2: Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

#Kurslarim, Tum Kurslar, Kariyer ve SSS ====> String
#Profil resmi ustune tiklandiginda cikan kisim ====> Liste
#Profil duzenledeki ad, soyad, sifre ====> String
#Kart bilgisi kismindaki;
#kart adi ====> String,
#Kart No, CVC ve PK ====> Int,
#ulke ====> Liste


#Soru3: Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.


dict2 = {"email": "ceren@gmail.com", "sifre": "qwerty"}

kullanici_email = input("Lutfen email adresinizi giriniz. ")
kullanici_sifre = input("Lutfen sifrenizi giriniz ")

if kullanici_email == dict2["email"] and kullanici_sifre == dict2["sifre"]:
    print("Giris yapildi")
elif kullanici_email != dict2["email"] and kullanici_sifre == dict2["sifre"]:
    print("Yanlis email girdiniz")
elif kullanici_email == dict2["email"] and kullanici_sifre != dict2["sifre"]:
    print("Yanlis sifre girdiniz")
else:
    print("Yanlis mail adresi ve sifre girdiniz")
