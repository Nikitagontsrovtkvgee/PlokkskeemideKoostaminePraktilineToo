from time import *
#V5  3.  R�hm 20 �pilast sooritas �he sessiooni jooksul kolm eksamit. Tehke algoritm eksamivormi t�itmiseks.
for � in range(20):
    print(f"Sooritab eksamit {�+1}, �pilane")
    for e in range(3):
        print(f"{e+1}. eksam")
#V4  2. Koostage programmi plokkskeem, et arvutada ainult negatiivsete P antud arvude summa.
#1 variable
try:
    vastus = 0
    P = int(input("Mitu korda kordame? "))
    while True:
        try:
            arv = float(input("Sisesta arv: "))
            if arv < 0:
                vastus += arv
        except ValueError:
            print("Viga: Palun sisestage korrektne number.")
        P -= 1
        if P == 0:
            break
    print(vastus)
except ValueError:
    print("Viga: Palun sisestage korrektne t�isarv P.")

#2 variable
try:
    vastus = 0
    P = int(input("Mitu korda kordame? "))
    for i in range(P):
        try:
            arv = float(input("Sisesta arv: "))
            if arv < 0:
                vastus += arv
        except ValueError:
            print("Viga: Palun sisestage korrektne number.")
    print(f"Summa on: {vastus}")
except ValueError:
    print("Viga: Palun sisestage korrektne t�isarv P.")


#V1  4. Koostage plokkskeem kotlette praadiva roboti jaoks.
try:
    kokku = 100
    panni_maht = 6
    aeg = 1
    lahenemine = kokku // panni_maht
    jaak = kokku % panni_maht
    if jaak > 0:
        lahenemine += 1
    print(f"Praeme. Tuleb {lahenemine} lahenemist.")
    for l in range(lahenemine):
        if jaak > 0 and l == lahenemine - 1:
            print(f"Panni peal on {jaak} kotlet.")
        else:
            print(f"Panni peal on {panni_maht} kotlet.")
        print(f"{l+1}. lahenemine. Praeme esimene pool")
        sleep(aeg)
        print("�mberp��rame")
        print(f" {l+1}. lahenemine. Praeme teine pool")
        sleep(aeg)
        print("Valmis!")
    print("K�ik kotletid on praetud")
except Exception as e:
    print(f"Tekkis viga: {e}")



#V2� � 2. Kirjutage programm, mis k�sib t�isarvu ja v�ljastab mis tahes selle v��rtuse, v�lja arvatud13. Kui antud arv on13, siis tr�kitakse selle asemel arv 77.
num = int(input("Sisestage t�isarv: "))

try:
    num = int(input("Sisestage t�isarv: "))
    print(77 if num == 13 else num)
except ValueError:
    print("Viga: Palun sisestage t�isarv.")

#V6�1. M��rake ja v�ljastage kahest sisendarvust suurem.
try:
    a = int(input("Sisestage esimene arv: "))
    b = int(input("Sisestage teine arv: "))
    maksimum = max(a, b)
    print("Suurem arv on:", maksimum)
except ValueError:
    print("Viga: Palun sisestage t�isarvud.")