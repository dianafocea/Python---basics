# Tema 5 - OOP _ Clase & Obiecte  - pt toate clasele creati cate 2 obiecte
# cu val diferite si apelati toate metodele clasei
# Exerciții obligatorii - grad de dificultate: Usor spre Mediu .
print("--------------------- 1.Clasa Cerc----------------------------\n")

# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()
from math import *

class Cerc():
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare
            
    def descriere_cerc(self):
        print(f"Cercul are culoarea {self.culoare} si raza = {self.raza}")
        
    def arie_cerc(self):
        return pi * (self.raza ** 2)

    def diametru_cerc(self):
        return self.raza * 2

    def circumferinta_cerc(self):
        return 2 * pi * self.raza

    def descriere_metode(self):  # metoda separata pt verificarea tuturor metodelor cercului
        print(f"Aria cercului = {self.arie_cerc()}, diametrul = {self.diametru_cerc()}, circumferinta = {self.circumferinta_cerc()} ")

c1 = Cerc(5, "fuchsia")
c1.descriere_cerc()
c1.descriere_metode()
print("-"*50)
print("--------------------- 2.Clasa Dreptunghi----------------------------\n")

# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic, dar
# va lua ca parametru o nouă culoare și va suprascrie atributul self.culoare.
# Verificam schimbarea culorii prin apelarea metodei descrie().

class Dreptunghi():
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def schimba_culoarea(self, culoare_noua):
        self.culoare = culoare_noua

    def arie_dreptunghi(self):
        return self.lungime * self.latime

    def perimetru_dreptunghi(self):
        return self.lungime + self.latime

    def descriere_dreptunghi(self):
        print(f"Dreptunghiul are lungimea = {self.lungime}, latimea = {self.latime}, "
              f"culoarea = {self.culoare}")

d1 = Dreptunghi(5, 3.5, "grena")
d1.descriere_dreptunghi()
d1.schimba_culoarea("turcoaz")
d1.descriere_dreptunghi()
d1.schimba_culoarea("orange")
d1.descriere_dreptunghi()
print("===================")
d2 = Dreptunghi(5, 3.5, "verde")
d2.descriere_dreptunghi()
d2.schimba_culoarea("galben")
d2.descriere_dreptunghi()

print("--------------------- 3.Clasa Angajat----------------------------\n")

# Atribute + constructor: nume, prenume, salariu
# Metode: nume_complet(), salariu_lunar(), salariu_anual(),
#  descrie(), marire_salariu(proc)

class Angajat():
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
        self.tichete = 500 #am adaugat un atribut ajutator pentru a testa functionalitatea metodelor

    def nume_complet(self):
        return f'{self.nume} {self.prenume}'

    def salariu_lunar(self):
        return self.salariu + self.tichete

    def salariu_anual(self):
        return self.salariu_lunar() * 12

    def marire_salariu(self, proc):
        self.salariu = self.salariu + (self.salariu * proc / 100)
        print(f"Salariul marit cu {proc}%: {self.salariu} lei")

    def descriere(self):
        print(f"Angajat: {self.nume_complet()}, salariu_baza: {self.salariu} lei, "
              f"salariu_lunar: {self.salariu_lunar()}, salariu_anual: {self.salariu_anual()}")

a1 = Angajat("Soare", "Alexandru", 6000)
a1.descriere()
a1.marire_salariu(5)
a1.descriere()

print("--------------------- 4.Clasa Cont----------------------------\n")

# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma), creditare_cont(suma)
class Cont():
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul `{self.titular_cont}` are in contul {self.iban} suma de {self.sold} £')

    def creditare_cont(self, suma):
        self.sold += suma
        print(f"Ati adaugat {suma} £, sold disponibil: {self.sold} £")

    def debitare_cont(self, suma):
        if suma > 0:
            if self.sold > 0:
                if self.sold >= suma:
                    self.sold -= suma
                    print(f"Ati retras {suma} £, sold disponibil: {self.sold} £")
                else:
                    print(f"Nu aveti minim {suma} £ in cont!")
            else:
                print("Sold 0, nu puteti retrage bani!")
        else:
            print("Fonduri insuficiente!")


c1 = Cont("RO34", "Mihnea Stefania", 100)
c1.afisare_sold()
c1.debitare_cont(100)
c1.creditare_cont(10)
c1.debitare_cont(-5)
c1.debitare_cont(10)
c1.afisare_sold()


# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.
print("--------------------- 1.Clasa Factura----------------------------\n")

# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
#
# ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x numar y
# Data: generați automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/
from datetime import *
from prettytable import *
from tabulate import tabulate

today = date.today()
class Factura():
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc
        self.seria = "XYZ"

    def schimba_cantitatea(self, cantit):
        self.cantitate = cantit

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def genereaza_factura(self):
        print((f"\tFactura {self.seria}-{self.numar} / {today}"))
        total = self.cantitate * self.pret_buc
        descriere = ["Produs", "Cantitate", "Pret bucata", "Total"]
        tabel = [[self.nume_produs, self.cantitate, self.pret_buc, total]]
        print(tabulate(tabel, descriere, tablefmt='grid', numalign="center"))

f2 = Factura(5778787, "Bec led", 8, 43)
f2.genereaza_factura()
f2.schimba_nume_produs("Creveti")
f2.schimba_pretul(65)
f2.schimba_cantitatea(10)
f2.genereaza_factura()
print("--------------------- 2.Clasa Masina----------------------------\n")

# Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
# culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
# negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0
class Masina():

    def __init__(self, model, viteza_max):
        self.marca = "Ford"
        self.model = model
        self.viteza_max = viteza_max
        self.viteza_actuala = 0
        self.culoare = "gri"
        self.culori_disp = {"galben", "rosu", "albastru", "verde", "visiniu", "negru"}
        self.inmatriculata = False

    def descriere(self):
        print(f"Fabrica {self.marca} - Craiova are disponibil modelul {self.model}, "
              f"viteza_actuala = {self.viteza_actuala}, viteza_max {self.viteza_max} km/h, "
              f"culoarea {self.culoare}, inmatriculata: {self.inmatriculata}")

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, culoare):
        if culoare in self.culori_disp:
            self.culoare = culoare
            print(f"Masina va avea culoarea `{culoare}` ")
        else:
            print(f"Nu avem dsponibila culoarea `{culoare}` ")

    def accelereaza(self, viteza):
        if 0 < viteza <= self.viteza_max:
                self.viteza_actuala = viteza
                print(f'masina a accelerat, viteza actuala este:{self.viteza_actuala}')
        elif viteza <= 0:
            print('nu se admit valori <= 0!')
        elif viteza > self.viteza_max:
            self.viteza_actuala = self.viteza_max
            print(f'masina a accelerat, viteza actuala este:{self.viteza_actuala}')

  #VARIANTA 2 --> accelereaza:

        # if 0 < viteza <= 190:
        #     self.viteza_actuala += viteza
        #     if 0 < self.viteza_actuala <= 190:
        #         print(f"ati accelerat cu {viteza} iar viteza actuala = {self.viteza_actuala} km/h")
        #     elif self.viteza_actuala > 190:
        #         self.viteza_actuala = self.viteza_max
        #         print(f"Ati atins deja viteza maxima, veti ramane la {self.viteza_actuala} km/h")
        # elif viteza > 190:
        #     self.viteza_actuala = self.viteza_max
        #     print(f"Ati atins deja viteza maxima, veti ramane la {self.viteza_actuala} km/h")
        # else:
        #     print(f"Nu se admit valori <= 0, veti ramane la viteza_actuala {self.viteza_actuala} km/h")

    def franeaza(self):
        if self.viteza_actuala <= 0:
            print(f"Nu mai puteti frana, deja viteza actuala = {self.viteza_actuala} km/h")
        else:
            self.viteza_actuala = 0
            print(f"Ati franat, aveti {self.viteza_actuala} km/h")

m1 = Masina("Kuga", 190)
m1.descriere()
m1.vopseste("roz")
m1.vopseste("rosu")
m1.inmatriculare()
m1.franeaza()
m1.accelereaza(-90)
m1.accelereaza(50)
m1.franeaza()
m1.franeaza()
m1.accelereaza(45)
m1.accelereaza(50)
m1.accelereaza(150)
m1.accelereaza(20)
m1.franeaza()
m1.descriere()

print("--------------------- 3. Clasa TodoList----------------------------\n")

# Atribute: todo{nume:descriere}
#(dict--> cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol
# și nu avem nevoie de constructor
# Metode:
# ● adauga_task(nume, descriere) - se va adauga in dict
# ● finalizează_task(nume) - se va sterge din dict
# ● afișează_todo_list() - doar cheile
# ● afișează_detalii_suplimentare(nume_task) -
# în funcție de numele taskului,
# printăm detalii suplimentare.

# ○ Dacă taskul nu e în todo list, întrebam
#  utilizatorul dacă vrea să-l adauge.
# ○ Dacă acesta răspunde nu - la revedere
# ○ Dacă răspunde da - îi cerem detalii task și
# salvăm nume+detalii în dict
class TodoList():
    todo = {}

    def adauga_task(self, nume, descriere):    #se va adauga in dict
        self.todo[nume] = descriere

    def finalizeaza_task(self, nume):    # - se va sterge din dict
        self.todo.pop(nume)
        print(f"Task ul `{nume}` a fost sters din lista")

    def afișează_todo_list(self):   # - doar cheile
        print("lista task-uri:", self.todo.keys())

    def afișează_detalii_suplimentare(self, nume_task):  #- în funcție de numele taskului printăm detalii suplimentare.
        if nume_task not in self.todo.keys():  # Dacă taskul nu e în todolist
            opt = input(f"Adaugati `{nume_task}`? [Da/Nu]: ").lower() # întrebam utilizatorul dacă vrea să-l adauge
            if opt == "da":  # Daca DA il intrebam detalii task si salvam detalile+nume in dict
                descr_task = input("Detalii task: ").lower()
                self.adauga_task(nume_task, descr_task)
                print(f"Task ul `{nume_task}` a fost adaugat in lista")
            else:
                print("Nu s-a adaugat task-ul. La reveredere!")
        else:
            if nume_task in self.todo.keys():
                print(f"{nume_task} --> {self.todo[nume_task]}")
        print(f"Elementele dictionarului:\n{self.todo}")

t1 = TodoList()
print("dictionarul initial este gol:", t1.todo)
t1.adauga_task("gatit", "bucatarie")
t1.adauga_task("teme", "python")
t1.adauga_task("shopping", "online")
print("dictionarul populat:", t1.todo)
print("-------------------------------------")
t1.afișează_todo_list()
print("`````````````````````````````````````")
t1.afișează_detalii_suplimentare("teme")
print("-------------------------------------")
t1.afișează_detalii_suplimentare("asculta muzica")
t1.afișează_detalii_suplimentare("vizioneaza film")
t1.finalizeaza_task("teme")
t1.afișează_todo_list()
