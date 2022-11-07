# Exerciții obligatorii - grad de dificultate: Usor spre Mediu .
# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']
#for simplu
for x in masini:
    print(f'Mașina mea preferată este {x}.')

#forEach
for masina in masini:
    print(f'Mașina mea preferată este {masina}.')

#while
x = 0
while x < len(masini):
    print(f'Mașina mea preferată este {masini[x]}.')
    x += 1

# 2. Aceeași listă:
# Folosește un for else
# În for:
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.

print('lista initiala: ', masini)
for i in range(1, len(masini)-1):
    masini[i] = masini[i].upper()
else:
    print('lista modificata: ', masini)

# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘
#
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel'] #varianta cu Mercedes
masini = ['Audi', 'Volvo', 'BMW', 'Ford', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']    #varianta fara Mercedes
for m in masini:
    if m == "Mercedes":
        print(f"Am gasit masina dorita de dvs: {m}")
        break
    else:
        print(f"Am gasit masina {m}.Mai cautam")
        continue

# 4. Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.
#
for m in masini:
    if m == "Trabant" or m == "Lăstun":
        continue
    print(f'S-ar putea să vă placă mașina {m}.')
#
# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# ● Printează Modele vechi: x.
# ● Modele noi: x.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
masini_vechi = []
i = 0
while i < len(masini):
    if masini[i] == 'Trabant' or masini[i] == 'Lăstun':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
    i += 1
print(f"masini_vechi: {masini_vechi}")
print(f"masini: {masini}")

# 6.
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin lista dictionarului.
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
print("Masinile disponibile sunt:")
for i, j in pret_masini.items():
    print(i, j)
print('-----------------------------------------------------')
print("Pentru un buget de sub 15.000 euro puteți alege mașina:")

for i, j in pret_masini.items():
    if j < 15000:
        print(f'{i} cu pretul: {j} euro')

# 7. Având lista:
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
contor = 0
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for num in numere:
    print(num, end=" | ")
    if num == 3:
        contor += 1
print(f"\nnr 3 apare de {contor} ori")
# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
suma = 0
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for num in numere:
    suma += num
print(f"\nsuma nr este {suma} ")
# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
nr_max = 0
for i in numere:
    if nr_max < i:
        nr_max = i
print(f"\ncel mai mare nr din lista este {nr_max} ")
# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.
numere = [7, 5, 3, 9, 3, 3, 1, 0, -4, 3]
print(numere)
print('Noua lista este: ')
for i in numere:
    if i > 0:
        i *= -1
    print(i, end=" ")
# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need
# Google.
# 1.   # Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișeaza cele 4 liste la final
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for i in alte_numere:
    if i % 2 == 0:
        numere_pare.append(i)
    else:
        numere_impare.append(i)
    if i > 0:
        numere_pozitive.append(i)
    else:
        numere_negative.append(i)

print("numere_pare: ", numere_pare)
print("numere_impare: ", numere_impare)
print("numere_pozitive: ", numere_pozitive)
print("numere_negative", numere_negative)
#
# 2. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
# Te poți inspira vizual de aici.
# https://www.youtube.com/watch?v=lyZQPjUT5B4
nr = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
while True:
    for i in range(0, len(nr)-2):
        for j in range(1, len(nr)-1):
            if nr[j] > nr[j + 1]:
                temp = nr[j]
                nr[j] = nr[j + 1]
                nr[j + 1] = temp
    print("Bubblesort:", nr)
    break
# 3. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
# Programul îi spune:
# ● Nr secret e mai mare
# ● Nr secret e mai mic
# ● Felicitări! Ai ghicit!
import random as r

numar_ghicit = None
while numar_ghicit == None:
    numar_secret = r.randint(1, 30)
    numar_ghicit = int(input("Alege un nr din intervalul (1, 30)!"))
    if numar_ghicit in range(1, 31):
        if numar_ghicit == numar_secret:
            print("Felicitări! Ai ghicit!")
        elif numar_ghicit > numar_secret:
            print(f'Nr secret e mai mic --> {numar_secret}')
        else:
            print(f'Nr secret e mai mare --> {numar_secret}')

    else:
        print("Ai ales un nr din afara intervalului!")
print("***********")
# 4. Alege un număr de la tastatură
# Scrie un program care să genereze în consolă următoarea piramidă
# spre exemplu pt n = 3:
# 1
# 22
# 333
n = int(input("Alege un nr din intervalul (1, 10)!"))
if 1 <= n < 10:
    for i in range(0, n+1):
        for j in range(0, i ):
            print(i, end="")
        print("\n", end="")
else:
    print("nr este in afara intervalului")
# 5.
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for)
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
for i in tastatura_telefon:
    print(f'Lista este: {i}')
    for j in i:
        print(f'cifra curenta este: {j}')

# *********************** TEMA EXTRA *********************** TEMA EXTRA ***********************

"""
ex 1 tema_extra:

Scrie un program care citeste de la tastatura 3 numere: a, b, c
Verifica cate numere intre a si b sunt divizibile cu c
"""
a = int(input("a = "))
b = int(input("b = introdu un nr > a:"))
c = int(input("introdu un nr > 0: "))
list_nr = range(a, b+1)
nr_divizibile = []
if a > b or a == b:
    print("\ninterval invalid! Alege b>a!")
elif c == 0:
    print("\nNu se poate imprati la zero!!!")
else:
    for i in list_nr:
        if i % c == 0:
            nr_divizibile.append(i)
            i += 1
    for i in list_nr:
        print(i, end="|")
    print(f"\nintervalul contine {len(nr_divizibile)} numere divizibile cu {c}: {nr_divizibile}")
"""
ex 2 tema_extra:
Scrieti un program prin care un user introduce de la tastatura o serie de numere integer, unul dupa altul folosind ENTER. Userul poate introduce cate numere vrea.
Cand userul introduce de la tastatura cuvantul "stop" in loc de un numar atunci programul ar trebui sa se opreasca si sa afiseze:
- toate numerele introduse sortate crescator
- cate numere pare au fost introduse si suma lor

Folositi continue si break
"""
lista_nr = []
while True:
    nr = input("Introduceti un nr sau cuvantul 'stop': ")
    if nr.lower() == "stop":
        break
    elif not nr.lstrip('-').isdigit():
        if nr.replace('.', '', 1).lstrip('-').isdigit():
            print("Nu sunt permise nr de tip float, ci doar integer!")
        else:
            print("Nu ai introdus un nr, mai incearca!")
        continue
    else:
        lista_nr.append(int(nr))
lista_nr.sort()
contor = 0
suma = 0
for nr in lista_nr:
    if nr % 2 != 0:
        continue
    contor += 1
    suma += nr
print(f"lista_nr introduse: {lista_nr}")
print(f"{contor} nr pare au fost introduse, iar suma lor este {suma}")
"""
ex 3 tema_extra:
Scrabble este un joc în care jucătorii obțin puncte scriind cuvinte. 
Cuvintele sunt punctate prin adunarea valorilor punctuale ale fiecărei litere individuale. 
Scrieti un program care ia ca intrare un cuvânt șir și returnează scorul scrabble echivalent pentru acel cuvânt.
"""
score = {
    "a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
    "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
    "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
    "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
    "x": 8, "z": 10
}
suma = 0
user_inp = input("Introduceti un cuvant/sir de cuvinte: ").lower
for i in user_inp:
    if i in score:
        print(f'Litera {i} are {score[i]} puncte')
        suma += score[i]
print(f"Punctajul pentru cuvantul/sirul `{user_inp}` este:", suma)
"""
ex 4 tema_extra:

Scrieți un program Python care repetă numerele întregi de la 1 la 50. 
Pentru multiplii de trei tipăriți „Fizz” în loc de număr, iar pentru multiplii de cinci tipăriți „Buzz”. 
Pentru numerele care sunt multipli de trei și cinci, se afișează „FizzBuzz”
"""
for i in range(1, 51): #1,2,3,4,5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    if i % 3 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    else:
        print(i)