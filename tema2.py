# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if - else.
'''
In cadrul unui if se executa anumite comenzi cand conditia este adevarata,
iar pe ramura else se executa alte comenzi daca o conditie este falsa
'''
print("-" * 50)

# 2. Verifică și afișează dacă x este număr natural sau nu.
x = float(input("introduceti o valoare pentru x: "))
if x >= 0 and x == int(x):
    print("numarul introdus este natural")
else:
    print("numarul introdus nu este natural")

print("-" * 50)

# # 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
x = int(input("introduceti o valoare pentru x: "))
if x > 0:
    print("numarul introdus este pozitiv")
elif x < 0:
    print("numarul introdus este negativ")
else:
    print("numarul introdus este neutru")

print("-" * 50)

# 4. Verifică și afișează dacă x este între -2 și 13.

x = int(input("introduceti o valoare pentru x: "))
if -2 <= x <= 13:  #  x >= -2 and x <= 13  /// iau in considerare interval inchis la ambele capete:
    print(f" {x} este cuprins între [-2 și 13]")
else:
    print(f" {x} nu este cuprins între [-2 și 13]")
print("-" * 50)


# # 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
x = int(input("introduceti o valoare pentru x: "))
y = int(input("introduceti o valoare pentru y: "))

if (x - y) < 5:
    print("diferența dintre x și y este mai mică de 5.")
else:
    print("diferența dintre x și y e mai mare sau egala cu 5.")
print("-" * 50)

##6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
x = int(input("introduceti o valoare pentru x: "))
if not(5 <= x <= 27): # iau in considerare interval inchis la ambele capete:
    print("x nu este cuprins în [5, 27]")
else:
    print("x este cuprins în [5, 27]")
print("-" * 50)

## 7.
# # x și y (int). Verifică și afișează dacă sunt egale,
# #iar dacă nu sunt, afișează care din ele este mai mare.

x = int(input("introdu o valoare pt x: "))
y = int(input("introdu o valoare pt y: "))
if x == y:
    print(f" x = y ({x} = {y})")
elif x < y:
    print(f" x < y ({x} < {y})")

else:
    print(f" x > y ({x} > {y})")

print("-" * 50)
# 8.
# X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.

x = int(input("introdu o valoare pt latura x, mai mare decat zero: "))
y = int(input("introdu o valoare pt latura y, mai mare decat zero: "))
z = int(input("introdu o valoare pt latura z, mai mare decat zero: "))

if x > 0 and y > 0 and z > 0:
    if x == y == z:
        print("Triunghiul este echilateral")
    elif x != y != z:
         print("Triunghiul este oarecare")
    else:
        print("Triunghiul este isoscel")
else:
    print("Introduceti pentru x, y si z valori mai mari decat 0!")

print("-" * 50)

# 9. Citește o literă de la tastatură. Verifică și afișează dacă este vocală sau nu
vocale = 'aeiou'
litera = input("introduceti o singura litera pt a verifica daca este vocala sau nu: ").lower()


if litera.isalpha() == True:
    if len(litera) == 1:
        if litera in vocale:
            print(f"Litera `{litera}` este o vocala")
        else:
            print(f"Litera `{litera}` este o consoana")
    else:
        print("Introduceti o singura litera!")  # nu este acceptat un cuvant intreg
else:
    print("Introduceti doar o litera, fara alte caractere!")  # nu sunt acceptate stringuri ori alte caractere decat litere
print("-" * 50)

# 10.Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

nota = float(input("introdu nota: "))
#
if 0 <= nota <= 10:
    if nota >= 9:
        print(f"nota {nota} reprezinta calificativul `A` ")
    elif nota >= 8:
        print(f"nota {nota} reprezinta calificativul `B` ")
    elif nota >= 7:
        print(f"nota {nota} reprezinta calificativul `C` ")
    elif nota >= 6:
        print(f"nota {nota} reprezinta calificativul `D` ")
    elif nota > 4:
        print(f"nota {nota} reprezinta calificativul `E` ")
    elif nota <= 4:
        print(f"nota {nota} reprezinta calificativul `F` ")
else:
    print("introduceti o nota valida in intervalul [0,10]!")

# print("-" * 50)

# Exerciții Opționale - grad de dificultate: Mediu spre greu - might need Google.
# 1.Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

num = int(input("introduceti un numar: "))
count = 0
x = num
if num == 0:
        print("Introduceti un numar diferit de 0!")
else:
        while num != 0:
                num = abs(num)
                num //= 10
                count += 1
        if count == 1:
            print(f"numarul {x} nu are minim 4 cifre, are doar o cifra!")
        elif 1 < count < 4 :
            print(f"numarul {x} nu are minim 4 cifre, are doar {count} cifre!")
        elif count == 4:
                print(f"numarul {x} are 4 cifre")
        else:
            print(f"numarul {x} are cel putin 4 cifre (are {count} cifre)")

# metoda a doua:
x = int(input("Introduceti un numar:  "))

if -999 <= x <= 999:
    print('Nu are minim 4 cifre')
else:
    print('Are minim 4 cifre')

print("-" * 50)

# 2.Verifică dacă x are exact 6 cifre.
#
numar = int(input("introduceti un numar nenul! :"))
x = numar
contor = 0
if numar == 0:
        print('introduceti un numar nenul!')
else:
        while numar != 0:
                numar = abs(numar)
                numar //= 10
                contor += 1

        if contor == 6:
                print(f'numarul {x} are exact 6 cifre!' )
        else:
                print(f'numarul {x} NU are 6 cifre!')

# metoda a doua
if x >= 100000 and x <= 999999:
    print('numarul are exact 6 cifre')
elif x >= -999999 and x <= -100000:
    print('numarul are exact 6 cifre')
else:
    print('numarul nu are exact 6 cifre')

# metoda a treia:
x = str(x)
if(x[0] == "-"):
    x = x[1:]

if len(x) == 6:
    print('are 6 cifre')
else:
    print('nu are 6 cifre')


print("-" * 50)

# 3.Verifică dacă x este număr par sau impar (x e int).

nr = int(input("introduceti un numar: "))
x = nr
if nr % 2 == 0:
        print(f" numarul {x} este par!")
else:
        print(f" numarul {x} este impar!")

print("-" * 50)

## 4. x, y, z (int).  Afișează care este cel mai mare dintre ele?
x = int(input("x =  "))
y = int(input("y =  "))
z = int(input("z =  "))

valori = x, y, z
print(f"maximul dintre dintre numerele {x}, {y}, {z} este: ")
maxim = x
if y > maxim:
    maxim = y
if z > maxim:
    maxim = z
print(maxim)

#metoda a doua:
if x >= y and x >= z:
    print(f'{x} este cel mai mare numar')
elif y >= x and y >= z:
    print(f'{y} este cel mai mare numar')
else:
    print(f'{z} este cel mai mare numar')

print("-" * 50)


# 5.
# X, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.

x = int(input("x =  "))
y = int(input("y =  "))
z = int(input("z =  "))

######// *** unghiurile trebuie sa fie diferite in interval deschis (0,180)
######// *** suma unghiurilor trebuie sa fie 180

print(f"valorile unghiurilor unui triunghi sunt: {x},{y},{z}")
if 0 < x < 180 and 0 < y < 180 and 0 < z < 180 and x + y + z == 180:
        print('triunghiul este valid')
else:
        print('triunghiul NU este valid, introduceti valori corespunzatoare!')

print("-" * 50)

## 6 ● Citiți de la tastatură un int x
##● Afișează stringul fără ultimele x caractere
##Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
#
str_ex = 'Coral is either the stupidest animal or the smartest rock'
x = int(input("introdu un numar: "))
lungime = len(str_ex)
str_nou = str_ex[:-x]

if x > 0 and x < lungime:
        print(str_nou)
else:
        print(f"alege un numar mai mare decat 0 si mai mic decat lungimea stringului (stringul are {lungime} caractere)")

print("-" * 50)


# 7.Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5
string_ex = 'Coral is either the stupidest animal or the smartest rock'
string_nou = string_ex[:5] + (string_ex[-5:])
print(string_nou)

print("-" * 50)

# 8. Același string.
# ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
# este o funcție care te ajuta sa faci asta)
# ● Folosind această variabilă + slicing, afișează tot stringul până la acest
# cuvant
# ● output: 'Coral is either the stupidest animal or the smartest '


str_full = 'Coral is either the stupidest animal or the smartest rock'
lungime = len(str_full)
print("lungime = ", lungime)

indx_rock = str_full.find("rock")  # salvam intr-o variabila indexul la care incepe subsirul `rock` --> 53
print("subsirul `rock` incepe la indexul: ", indx_rock)

sliced_str = slice(indx_rock)
subsir = str_full[sliced_str] # afisa variabila subsir (noul string pana la inceperea substringului `rock`)
print("output: ", subsir)
print(len(subsir))    # noul sir are 53 caractere

new_str = str_full[:indx_rock]   # alta metoda pt a afisa stringul pana la inceperea substringului `rock`
print(new_str == subsir)     #verificare prin cele 2 metode

print("-" * 50)

# 9. Citește de la tastatura un string
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat
# #
str_input = input("introdu un string: ").lower()
assert str_input[0] == str_input[-1], "primul caracter NU este identic cu ultimul"
print("primul caracter este identic cu ultimul")

#print("-" * 50)

# 10. Avand stringul '0123456789'
# ● Afișați doar numerele pare
# ● Afișați doar numerele impare
# (hint: folositi slicing, controlați din pas)
#
#
string_nr = '0123456789'
lungime_nr = len(string_nr)
print("lungime str: ", lungime_nr)
nr_pare = slice(0, 10, 2)
pare = string_nr[nr_pare]
print("Nr pare sunt: ", pare)
nr_impare = slice(1, 10, 2)
impare = string_nr[nr_impare]
print("Nr impare sunt: ", impare)

#metoda a doua:
word = '0123456789'
print(word[0::2])
print(word[1::2])
#print("-" * 50)

# Exerciții Bonus (may need google) .
# 11. Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
#
# Luați un numărul ghicit de la utilizator
# Verificați și afișați dacă utilizatorul a ghicit
# Veți avea 3 opțiuni
# ● Ai pierdut. Ai ales un dice_roll mai mic. Ai ales x dar a fost y
# ● Ai pierdut. Ai ales un dice_roll mai mare. Ai ales x dar a fost y
# ● Ai ghicit. Felicitari! Ai ales x si zarul a fost y
# #


import random as r
dice_roll = r.randint(1,6)
guess_nr = int(input("n = "))
if 1 <= guess_nr <= 6:
    if dice_roll != guess_nr:
        if guess_nr > dice_roll:
            print(f"Ai pierdut. Ai ales un dice_roll mai mare. Ai ales {guess_nr} dar a fost {dice_roll}")
        else:
            print(f"Ai pierdut. Ai ales un dice_roll mai mic. Ai ales {guess_nr} dar a fost {dice_roll}")
    else:
        print(f"Ai ghicit. Felicitari! Ai ales numarul {guess_nr} si zarul a fost {dice_roll}!")
else:
    print(f"Ai ales un numarul din afara intervalului inchis [1,6]!")
