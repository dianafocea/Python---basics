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


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    def get_latura(self):
        return self.__latura

    def set_latura(self, latura):
        self.__latura = latura

    def delete_latura(self):
        self.__latura = None

    def aria(self):
        print(f"latura = {self.__latura}.")
        if self.__latura == 0 or self.__latura == None:
            return ("Nu putem calcula aria unui patrat a carui latura = None sau zero!")
        else:
            return self.__latura ** 2

    #metoda descrie = metoda de clasa, care se mosteneste automat,
# fara a fi nevoie sa mai definim clasa descrie in copil
    def descrie(self):
        if self.__latura == 0 or self.__latura == None:
            print("Nu poate fi descrisa o figura geometrica cu latura 0 sau None")
        else:
            return super().descrie()

class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza


    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        self.__raza = raza

    def delete_raza(self):
        self.__raza = None

    def aria(self):
        print(f"raza = {self.__raza}.")
        if self.__raza == 0 or self.__raza == None:
            return (f"Nu putem calcula aria unui cerc a carei raza = None sau zero!")
        else:
            return self.PI * (self.__raza ** 2)

    def descrie(self):
        if self.__raza == 0 or self.__raza == None:
            print("Nu poate fi descrisa o figura geometrica cu latura 0 sau None")
        else:
            print('‘Eu nu am colturi’')

print(" ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ")
lst_frm_geom = [Patrat(1), Patrat(0), Patrat(None), Cerc(1), Cerc(None), Cerc(0)]
for f in lst_frm_geom:
    print(f'aria:  {f.aria()}')
    f.descrie()
    print(" ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ")

print(" ` ` ` ` ` ` patratul:` ` ` ` ` ` ` ` ` ` ` ` ` ` ")
p1 = Patrat(5)
print("aria p1 = ", p1.aria())
print('descrie p1:')
p1.descrie()
print("get_latura p1 = ", p1.get_latura())
p1.set_latura(2)
print("get_latura p1 dupa set: ", p1.get_latura())
print("delete_latura p1 = ", p1.delete_latura())
print("get_latura dupa delete = ", p1.get_latura())
print('descrie p1:')
p1.descrie()

print(" ` ` ` ` ` `cercul: ` ` ` ` ` ` ` ` ` ` ` ` ` ` ")

c1 = Cerc(5)
print("aria c1 = ", c1.aria())
print('descrie c1:')
c1.descrie()
print("get_raza c1 = ", c1.get_raza())
c1.set_raza(2)
print("get_raza c1 dupa set: ", c1.get_raza())
print("delete_raza c1 = ", c1.delete_raza())
print("get_raza dupa delete = ", c1.get_raza())
print('descrie c1:')
c1.descrie()







