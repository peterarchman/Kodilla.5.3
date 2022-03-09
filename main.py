class BaseContact:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email
    def contact(self):
        print("Wybieram numer", self.telefon, "i dzwonie do", self.imie, self.nazwisko)

    @property
    def label_lenght(self):
        return self.label_lenght

    @label_lenght.setter
    def label_lenght(self):
        return len(imie) + len(nazwisko)


class BusinessContact(BaseContact):
    def __init__(self, stanowisko, firma, telefon_sluzbowy, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefon_sluzbowy = telefon_sluzbowy

card1 = BaseContact(imie = "Jan", nazwisko = "Kowalski", telefon = "+48 5010505501", email = "jk@gg.pl")
card2 = BaseContact(imie = "Adam", nazwisko = "Rudy", telefon = "+48 6006006000", email = "dd@ff")
card3 = BaseContact(imie = "Zosia", nazwisko = "Nowak", telefon = "+48 50030004000" , email = "cww@wrr")

card4 = BusinessContact(imie = "Zbyszek", nazwisko = "Bielski", telefon = "+48 499999999",  firma = "HP", stanowisko = "sprzatacz", email = "wew@fv", telefon_sluzbowy = "+48111111111")
card5 = BusinessContact(imie = "Adrian", nazwisko = "Milski", telefon = "+48 111111111", firma = "LG", stanowisko = "junior dev", email = "fe@ww", telefon_sluzbowy = "+48333333333")
card6 = BusinessContact(imie = "Seba", nazwisko = "Maly", telefon = "+48 77777777", firma = "Google", stanowisko = "CEO", email = "fgg@hh", telefon_sluzbowy = "+48 22222222")

card1.contact()
card6.contact()

from faker import Faker
fake = Faker()

for i in range(5):
    print(fake.name())




