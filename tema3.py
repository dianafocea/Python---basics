# Tema 3 - Structuri de date:

# Exerciții obligatorii - grad de dificultate: Usor spre Mediu
# //Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
# Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# // X este un int.

# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# ● Afișeaz-o
# ● Inversează ordinea folosind slicing și suprascrie această listă.
# ● Printează varianta actuală (inversată).
# ● Pe această listă aplică o metodă care bănuiești că face același lucru,
# adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
# deoarece metoda face asta automat.
# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
# inițială.
# Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
# suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
#
# suprascrierea automat și permanentizează aceste modificări. Ambele variante
# își găsesc utilitatea în funcție de ce ne dorim în acel moment.

note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)
print(note_muzicale)

# 2. De câte ori apare ‘do’?
print(f'Nota `do` apare de {note_muzicale.count("do")} ori')

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.
lst1 = [3, 1, 0, 2]
lst2 = [6, 5, 4]
print(f' lst1 este: {lst1}')
print(f' lst2 este: {lst2}')
print("***********************************")

lst_total1 = lst1 + lst2
print(f' lst_total1 este: {lst_total1}')
lst_total2 = lst1.__add__(lst2)
print(f' lst_total2 este: {lst_total2}')
lst1.extend(lst2)
print(f' lst1 cu extend este: {lst1}')
lst1 = [3, 1, 0, 2]
lst2 = [6, 5, 4]
lst1 += lst2
print(lst1)
print(lst2)

# 4.
# ● Sortează și afișază lista generată la exercițiul anterior.
# ● Sterge numărul 0 folosind o funcție.
# ● Afișeaza iar lista.

lst_total1.sort()
print("lst sortata: ", lst_total1)
lst_total1.pop(0)
print("sterg nr 0: ", lst_total1)
lst_total2.sort(reverse=True)
lst_total2.remove(0)
print("sterg nr 0: ", lst_total2)
import random
print("Lungimea listei: ", len(lst_total2))
print("lst random: ", random.sample(lst_total2, 6))


# 5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
# ● Lista este goală.
# ● Lista nu este goală.

print("lista ex5: ", lst1)
if len(lst1) <= 0:
    print(f'Lista este goala', lst1)
else:
    print(f'Lista nu este goala', lst1)

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
print("ex6: ")
lst1.clear()
if len(lst1) <= 0:
    print(f'Lista este goala', lst1)
else:
    print(f'Lista nu este goala', lst1)

# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.
print("lista ex7: ", lst1)

if len(lst1) <= 0:
    print(f'Lista este goala', lst1)
else:
    print(f'Lista nu este goala', lst1)

# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print("ex8. elevii sunt: ", dict1.keys())

# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie

print("ex9: ")
for i, j in dict1.items():
    print(f'{i} a luat nota {j}')

#
# 10. Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare
#
dict1.update({"Dorel": 7})
print(dict1)

# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi
#
dict1.pop("Dorel")
print(dict1)
dict1.update({"Ionica": 9})
print(dict1)

# 12.
# Set
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# ● Adaugă în zilele_sapt ‘luni’
# ● Afișeaza zile_sapt

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

zile_sapt.add('luni')
print("zilele_sapt: ", zile_sapt)

# 13.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor săptămânii.
# ● Weekend nu este un subset al zilelor săptămânii.

if weekend.issubset(zile_sapt):
    print("weekend este un subset al zilelor săptămânii")
else:
    print("weekend nu este un subset al zilelor săptămânii")

# 14. Afișează diferențele dintre aceste 2 seturi.
print("diferenta dintre seturi:", zile_sapt.difference(weekend))

# 15. Afișază intersecția elementelor din aceste 2 seturi.
print("intersectia dintre seturi:", zile_sapt.intersection(weekend))

print("- " * 50)

# Exerciții Opționale - grad de dificultate: Mediu spre greu(may need google) .
# 1. Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
#
# ● Declară o Listă cu 5 jucători
# ● schimbari_efectuate = te joci tu cu valori diferite
# ● schimbari_max = 3
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# - Efectuează schimbarea
#
# - Șterge jucătorul scos din listă
# - Adaugă jucătorul intrat
# - Afișaza a intra x, a ieșit y, mai ai z schimbări
# Dacă jucătorul nu e în teren:
# - Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
# teren’
# - Afișază ‘mai ai z schimbări’
# Testează codul cu diferite valori
#
# Google search hint
# “how to check if item îs în list python”

jucatori = ["a", "b", "c", "d", "e"]
rezerve = ["x", "y", "w", "z"]
schimbari_efectuate = int(input("Alege 0, 1, 2 sau 3: "))  # testez exercitiul, pe rand, cu valorile  0, 1, 2, 3
schimbari_max = 3
schimbari_ramase = schimbari_max - schimbari_efectuate   # 3, 2, 1
print("schimbari_ramase: ", schimbari_ramase)
nume_jucator = input("Alege un nume_jucator dintre: a, b, c, d si e: ").lower()
nume_rezerva = input("Alege nume_rezerva dintre: x, y, w si z: ").lower()

if 0 < schimbari_ramase <= schimbari_max:  # 3, 2, 1
    if nume_jucator in jucatori:
        if nume_rezerva in rezerve:
            schimbari_efectuate += 1
            jucatori.remove(nume_jucator)
            jucatori.append(nume_rezerva)
            rezerve.remove(nume_rezerva)
            print(f"A intrat jucatorul `{nume_rezerva}` si a iesit jucatorul `{nume_jucator}`."
                  f" Mai ai {schimbari_max - schimbari_efectuate} schimbari disponibile!")
        else:
            print(f"Jucatorul `{nume_rezerva}` nu se afla in rezerva!")
    else:
       print(f"Jucatorul `{nume_jucator}` nu se afla in teren. Mai ai "
             f"{schimbari_max - schimbari_efectuate} schimbari disponibile!")
else:
    if nume_jucator in jucatori:
        print(f"Jucatorul `{nume_jucator}` se afla in teren, insa oricum nu se mai pot face schimbari!!!")
    else:
        print(f"Nu se poate efectua schimbarea deoarece jucatorul `{nume_jucator}` nu se afla in teren. Nu mai ai schimbari disponibile!")

print("*" * 50)
print(f"Jucatorii din teren sunt: {jucatori}")
print(f"Rezervele disponibile sunt: {rezerve}")