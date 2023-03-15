# Classes

# classes.py
class Banka:
    def krediBasvur(self):
        print("Kredi başvurusu yapıldı. ")

    def krediHesapla(self):
        print("Hesaplar yapıldı. ")
        
banka = Banka()
banka.krediBasvur

# self = this

# matematik.py
class Matematik:
    def __init__(self, sayi1, sayi2): #constructor (yapıcı) blok
        self.s1 = sayi1
        self.s2 = sayi2
        print("Matematik başladı (referansı oluştu)")
    def topla(self):
        return self.s1 + self.s2
    def cıkar(self):
        return self.s1 - self.s2
    def bol(self):
        return self.s1 / self.s2
    def carp(self):
        return self.s1 * self.s2

matematik = Matematik(6,7)
sonuc = matematik.bol()
print("Sonuç: " + str(sonuc))

class Istatistik(Matematik): #inheritance
    def __init__(self, sayi1, sayi2):
        super.__init__(sayi1, sayi2)
    def varyansHesapla(self):
        return self.s1 * self.s2
    


# person.py
class Person:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName

musteri1 = Person("Ceren", "Orhan")
musteri2 = Person("Ahmet", "Demiroğ")
musteri3 = Person("Kerem", "Varış")

print(musteri1.name)
