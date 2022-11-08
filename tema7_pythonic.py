from abc import ABC, abstractmethod
'''ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() --> aceasta printează pe ecran: 
‘Cel mai probabil am colturi’
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură
ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)
Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește 
field PI mostenit din clasa părinte (opțional, doar dacă ai ales
să implementezi metoda abstractă aria)
POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui
3. Actualizează proiectul pe github facand un push la noul cod
În folder-ul de teme ajunge să pui doar linkul cu proiectul tău public'''
class FormaGeometrica(ABC):
    PI = 3.14
    @abstractmethod
    def aria(self):
        pass

    @classmethod
    def descrie(self):
        print('`Cel mai probabil am colturi`')

print("PYthonic encaps:")

class PatratPy(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    def aria(self):
        print(f"latura = {self.__latura}.")
        if self.__latura == 0 or self.__latura == None:
            return ("Nu putem calcula aria unui patrat a carui latura = None sau zero!")
        else:
            return self.__latura ** 2

    def descrie(self):
        if self.__latura == 0 or self.__latura == None:
            print("Nu poate fi descrisa o figura geometrica cu latura 0 sau None")
        else:
            super().descrie()

    @latura.getter
    def latura(self):
        return self.__latura

    @latura.setter
    def latura(self, val):
        self.__latura = val

    @latura.deleter
    def latura(self):
        self.__latura = None


class CercPy(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    def aria(self):
        print(f"raza = {self.__raza}.")
        if self.__raza == 0 or self.__raza == None:
            return ("Nu putem calcula aria unui cerc a carei raza = None sau zero!")
        else:
            return self.__raza * (self.__raza ** 2)

    def descrie(self):
        if self.__raza == 0 or self.__raza == None:
            print("Nu poate fi descrisa o figura geometrica cu raza 0 sau None")
        else:
            print('‘Eu nu am colturi’')


    @raza.getter
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, val):
        self.__raza = val

    @raza.deleter
    def raza(self):
        self.__raza = None


print('`````````````````````````````````````````')

p1 = PatratPy(5)
print(f"descriere patrat: ")
p1.descrie()
print(f'aria patratului cu latura = {p1.latura}, aria este: {p1.aria()}')
print(f"latura patratului inainte de setter este: {p1.latura}")
p1.latura = 8
print(f'aria patratului dupa setter cu latura {p1.latura} = {p1.aria()}')
del p1.latura
print(f"latura dupa stergere: {p1.latura}")
p1.latura = 1
print(f"pt latura = {p1.latura}, aria este: {p1.aria()}")
p1.descrie()
del p1.latura
print(f"pt latura = {p1.latura}, aria este: {p1.aria()}")
p1.descrie()

print('`````````````````````````````````````````')

c1 = CercPy(5)
c1.descrie()
print(f'aria cercului cu raza = {c1.raza}, aria este: {c1.aria()}')
print(f"raza cercului inainte de setter este: {c1.raza}")
c1.raza = 8
print(f'aria cercului dupa setter cu raza {c1.raza} = {c1.aria()}')
del c1.raza
print(f"raza dupa stergere: {c1.raza}")
c1.raza = 1
print(f"pt raza = {c1.raza}, aria este: {c1.aria()}")
c1.descrie()
del c1.raza
print(f"pt raza = {c1.raza}, aria este: {c1.aria()}")
c1.descrie()