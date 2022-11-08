# Exerciții obligatorii - grad de dificultate: Usor spre Mediu .
# 1.Funcție care să calculeze și să returneze suma a două numere
def suma_numere(x, y):
    suma = x + y
    return (f'{x} + {y} = {suma}')
print(suma_numere(3,9))
# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
def is_bool(a, b):
    if a % b == 0:
        return True
    else:
        return False
print(is_bool(20, 4))

# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)
def nume_complet(nume, prenume, nume_mijlociu):
    return len(nume + prenume + nume_mijlociu)
print(f"numele complet este Focea Oana Diana iar totalul caracterelor este:")
print(nume_complet("Focea", "Oana", "Diana"))

# 4. Funcție care returnează aria dreptunghiului
def arie_dreptunghi(a, b):
    return a * b
print("aria dreptunghiului este:", arie_dreptunghi(6, 5))

# 5. Funcție care returnează aria cercului
#
from math import pi
def arie_cerc(r):
    return int(pi * (r ** 2))
print("aria cercului este:", arie_cerc(2))

# 6. Funcție care returnează True dacă un caracter x se găsește
# într-un string dat și False dacă nu găsește.
txt = input("Introdu un string: ")
ch = input("cauta un caracter in text: ")
def bool_char(x, y):
    if ch in txt:
        return True
    else:
        return False
print(bool_char(txt, ch))

# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y
txt = input("Type a string: ")
def void(txt):
    sum_lower = 0
    sum_upper = 0
    for letter in txt:
        if letter.islower():
            sum_lower += letter.count(letter)
        elif letter.isupper():
            sum_upper += letter.count(letter)
    print(f"Lower characters: {sum_lower}\nUpper characters: {sum_upper}")
void(txt)

# 8. Funcție care primește o LISTA de numere și returnează
# o LISTA doar cu numerele pozitive
lista = [10, -6, 8, -100, 9, 5, -8, 44, 4, -22, -1, 80, 35, 0]
lista_pare = []
def lista_pozitive(lista):
    for nr in lista:
        if nr % 2 == 0:
            lista_pare.append(nr)
    return lista_pare
print(lista_pozitive(lista))

# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.
def void(a, b):
    if a > b:
        print(f'{a} > {b}')
    elif a < b:
        print(f'{a} < {b}')
    else:
        print(f'{a} == {b}')
void(-0.3, -1)

# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False
setlist = {4, 7, -4, 33, 0, 8, 5, 85, 77, -1, -2, 100}
nr = int(input("Adauga un nr in set: "))
def add_set(nr, setlist):
    if nr in setlist:
        print(f"Nu am adaugat nr {nr} în set deoarece acesta există deja")
        return False
    else:
        print(f"Am adaugat nr {nr} în set")
        setlist.add(nr)
        return True
print(add_set(nr, setlist))

# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.
# 1. Funcție care primește o lună din an și returnează câte zile are acea luna
# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.
# 1. Funcție care primește o lună din an și returnează câte zile are acea luna
month_input = int(input("Choose a number between 1-12: "))
def days_per_month(m):
    months_dict = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    if m in months_dict:
        print(f'The month is {months_dict[m]} and the number of days are: ')
        if m in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        elif m == 2:
            return "28 or 29"
        else:
            return 30
    else:
        print(f"Month number ({m}) is out of range")
print(days_per_month(month_input))

# 2. Funcție calculator care să returneze 4 valori.
# Suma, diferența, înmulțirea, împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)
def calculator(x, y):
    def suma(x, y):
        return x + y
    def scadere(x, y):
        return x - y
    def inmultire(x, y):
        return x * y
    def impartire(x, y):
        return x / y
    a = suma(x, y)
    b = scadere(x, y)
    c = inmultire(x, y)
    d = impartire(x, y)
    print("Suma:", a)
    print("Diferenta:", b)
    print("Inmultirea:", c)
    print("Impartirea:", d)
    return a, b, c, d
a,b,c,d = calculator(20, 2)

# 3. Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
list_nr = [1, 3, 1, 5, 9, 7, 7, 5, 5]
def counting(x):
    counting_dict = {}
    num = range(0, 10)
    counting_dict = dict.fromkeys(num, 0)
    for nr in list_nr:
        if (nr in counting_dict):
            counting_dict[nr] += 1
        else:
            counting_dict[nr] = 1
    return counting_dict
print(counting(list_nr))

# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
def max_nr(x, y, z):
    if x >= y and x >= z:
        print('cel mai mare numar e: ')
        return x
    elif y >= x and y >= z:
        print('cel mai mare numar e: ')
        return y
    else:
        print('cel mai mare numar e: ')
        return z
print(max_nr(-8, 0, -4))

# 5. Funcție care să primească un număr și să returneze
# suma tuturor numerelor de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
num = int(input("Type a number: "))
def sum_all_numbers(n):
    sum = 0
    if num > 0:
        for i in range(0, num + 1):
            sum += i
        return sum
    else:
        return "Type a number greater than 0!"
print(sum_all_numbers(3))

# Exerciții Opționale - Bonus
# 1.Funcție care primește 2 liste de numere (numerele pot fi dublate).
# Returnați numerele comune
list1 = [0, 1, 2, 3, 4, 2, 3, 4, 9, 8, 7]
list2 = [0, 1, 2, 0, 2, 3, 4, 9, 0, 5, 6]
list3 = []
def intersection_lists(lst1, lst2):
    for nr in list1:
        if nr in list2:
            list3.append(nr)
    return set(list3)
print(intersection_lists(list1, list2))

# 2.. Funcție care să aplice o reducere de preț
# Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
# Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
# invalidă.
pret_produse = [10, 100, 4, 34, 55, 99.99, 5.99]
pret_redus = []
REDUCERE = 0.1
def discount():
    if REDUCERE:
        for pret in pret_produse:
            pret *= REDUCERE
            pret_redus.append(float(pret))
    else:
        print("Nu exista alta reducere decat de 10%!")
    return pret_redus
print(discount())

# 3. Funcție care să afișeze data și ora curentă din ro
# (bonus: afișați și data și ora curentă din China)
from datetime import datetime
import pytz
zones = pytz.all_timezones
print(zones)
def time_zone():
    name = input("enter `continent/city` for time_zone. Example1: America/New_York\n"
                 "Example2: for China time_zone type this format: Asia/Shanghai \n: ").title()
    if name in zones:
        my_tz = pytz.timezone(name)
        time_input = datetime.now(my_tz)
        my_current_tz = time_input.strftime("%A, %d %B %Y, %X %p ")
        print(f"The current datetime in {name} is: ")
        return my_current_tz
    else:
        return name + " not in timezone"
print(time_zone())

# 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
# Crăciun dacă nu vrei să ne zici cand e ziua ta :)
from datetime import *
today = date.today()
print("Today: " + today.strftime('%d, %b %Y'))
thisYear = today.year
my_birthday = date(thisYear, 11, 13)
def my_birthday_calculator():
    if today < my_birthday:
        print("my_next_birthday: " + my_birthday.strftime('%d, %b %Y'))
        delta = (my_birthday - today).days
        print("Days left until my_birthday: ")
        return str(delta)
    elif today == my_birthday:
        return "Today is my_birthday Day!"
    else:
        my_next_birthday = date(thisYear+1, 11, 13)
        print("my_next_birthday: " +  my_next_birthday.strftime('%d, %b %Y'))
        delta = (my_next_birthday - today).days
        print("Days left until next my_birthday:")
        return str(delta)
print(my_birthday_calculator())