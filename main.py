class Osoba:
    liczbaInstancji = 0
    def __init__(self,id=0,imie=""):
        self.__id = id
        self.__imie = imie
        Osoba.liczbaInstancji += 1
    def kopiowanie(self,o):
        return osoba(o.__id,o.__imie)
    def przywitanie(self,i):
        print("Cześć",i,"mam na imię",self.__imie)


print(Osoba.liczbaInstancji)
osoba1 = Osoba(1,"Jan")
osoba2 = osoba1.kopiowanie(osoba1)

print(osoba1.__dict__)
print(osoba2.__dict__)
osoba1.przywitanie("janusz")
print(Osoba.liczbaInstancji)
