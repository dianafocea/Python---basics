#Exerciții obligatorii - grad de dificultate: Ușor spre Mediu:
#1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.

'''
O variabila este o zona din memoria calculatorului
pe care o etichetam, in mod unic,
pentru a stoca valori
'''

# 2. Declară și initializează câte o variabilă din fiecare din urm tipuri de date :

nume = "avocado"  #str
bucati = 5  #int
pret = 5.5  #float
isFruit = True  #bool
print("-" *50)


# 3. Utilizează funcția "type" pentru a verifica dacă au tipul de date așteptat.

assert type(nume) == str, f"Variabila `nume` trebuie sa fie de tipul `str`, dar este de tipul: {type(nume)}"
print(f'Passed! Variabila "nume" este de tipul {type(nume)}')

assert type(bucati) == int, f"Variabila `bucati` trebuie sa fie de tipul `int`, dar este de tipul: {type(bucati)}"
print(f'Passed! Variabila "bucati" este de tipul {type(bucati)}')

assert type(pret) == float, f"Variabila `pret` trebuie sa fie de tipul `float`, dar este de tipul: {type(pret)}"
print(f'Passed! Variabila "pret" este de tipul {type(pret)}')

assert type(isFruit) == bool, f"Variabila `isFruit` trebuie sa fie de tipul `bool`, dar este de tipul: {type(isFruit)}"
print(f'Passed! Variabila "isFruit" este de tipul {type(isFruit)}')


print(type(nume))
print(type(bucati))
print(type(pret))
print(type(isFruit))
print("-" *50)


# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
# aceeași variabilă (suprascriere):
# - Verifică tipul acesteia.

print(f'Pretul rotunjit din {pret} este: {round(pret)}')
print("-" *50)

pret = round(pret)
print(f'Pretul suprascris este: {pret} si are tipul de date: {type(pret)}')
print("-" *50)


# 5. Folosește "print()" și printează în consola 4 propoziții folosind cele 4 variabile.

print(f'Variabila "nume" este de tipul: {type(nume)}')
print(f'Variabila "bucati" este de tipul: {type(bucati)}')
print(f'Variabila "pret" este de tipul: {type(pret)}')
print(f'Variabila "isFruit" este de tipul: {type(isFruit)}')
print("-" *50)

# 6.Citește de la tastatură:
# - numele;
# - prenumele.
# Afișează: 'Numele complet are x caractere'.

#*******  ma voi ajuta de metoda .upper pentru a evidentia cuvintele mai bine *********


nume = str(input("Introdu numele si prenumele: ")).upper()
numeNou = ((len(nume) - nume.count(" ")))

print(f'Numele este {nume} si are {numeNou} caractere.')
print("-" *50)


# 7. Citește de la tastatură:
# - lungimea;
# - lățimea.
# Afișează: 'Aria dreptunghiului este x'.

lungime = int(input("Introdu lungimea: "))
latime = int(input("Introdu latimea: "))
x = lungime * latime
print(f'Aria dreptunghiului este {x}')
print("-" *50)


# 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# - afișează de câte ori apare cuvântul 'the';

prop = 'Coral is either the stupidest animal or the smartest rock'
print(f'Cuvantul `the` apare de {prop.count("the")} ori')
print("-" *50)


# 9. Același string.
# ● inlocuieste "the" cu "THE" peste tot;
# ● Printează rezultatul.

#- printeaza de câte ori apare cuvântul 'the';

prop = 'Coral is either the stupidest animal or the smartest rock'
print(f'Cuvantul `the` apare de {prop.count("the")} ori')
new_prop = prop.replace("the", "THE")
print(new_prop)

print("-" *50)



# 10.******************
#Folosiți un assert ca să verificați dacă acest string conține doar numere.

prop = 'Coral is either the stupidest animal or the smartest rock'

#print(prop.isdigit()) #False
#print(prop == prop.isdigit())  #False
assert prop is not prop.isdigit(), "Variabila `prop` contine numere "
print('Passed! Variabila `prop` nu contine numere')

print("-" *50)

# *************** Exerciții Opționale - grad de dificultate: Mediu spre greu ***************

#ex 1. :
#- citește de la tastatură un string de dimensiune impară;
#- afișează caracterul din mijloc.

cuv = input("Introdu cuv de dimeniune impara: ")
#*******  ma voi ajuta de metoda .upper pentru a evidentia cuvintele mai bine *********

dimension = len(cuv)
middle = dimension // 2
letter = cuv[int(dimension / 2)]

if dimension % 2 == 0:
    print('please enter a string with an odd dimension')
else:
    print(f' The string {cuv.upper()} has middle index {middle}, middle letter is: {letter}')
print("-" *50)

#2. Folosind assert, verifică dacă un string este palindrom.

word = input('please type a word to check if is a palindrome: ')
new_word = word[::-1]
print(f'stringul `{word}` inversat este `{new_word}`')

assert word == new_word, 'cuvantul `{word}` nu este un palindrom ({new_word})'
print(f'stringul `{word}` este palindrom ({new_word})')
print("-" *50)

# 3. Folosind o singură linie de cod :
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.

car, version = input('Enter a car and a version: ').split(" "); print(f'your car is: {car}\ncar`s version: {version}')

print("-" *50)

# 4. Exercițiu:
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă
# cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
# caracter => alAbAlA portocAla.


# string_txt = input(" enter a string: ")
# first_ch = string_txt[0]
# transform = first_ch.lower() + string_txt[1:-1].replace(first_ch,first_ch.upper()) + string_txt[-1].lower()
# print(f'new string is: {transform}')

print("-" *50)

# 5.Exercițiu:
# - citește un user de la tastatură;
# - citește o parolă;
# - afișează: 'Parola pt user x este ***** și are x caractere';
# - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
# afișeze corect.
# eg: parola abc => ***
# parola abcd => ****


username = input("enter username: ")
password = input("enter password: ")
masked_password = "*" * len(password)
print(f'Parola pentru username `{username}` este: {masked_password} si are {len(password)} caractere')
