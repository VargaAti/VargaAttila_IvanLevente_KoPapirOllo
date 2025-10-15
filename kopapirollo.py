import random as r

folytatja = True

gep_pont = 0
fh_pont = 0


while folytatja:
    print(r"""
     _  __ ___        ____             __           ___  _ _   __  
    | |/ //_/_/      |  _ \ __ _ _ __ /_/_ __      / _ \| | | /_/  
    | ' // _ \       | |_) / _` | '_ \| | '__|    | | | | | |/ _ \ 
    | . \ |_| |      |  __/ (_| | |_) | | |       | |_| | | | (_) |
    |_|\_\___/       |_|   \__,_| .__/|_|_|        \___/|_|_|\___/ 
                                |_|                                 
    """)


    felhasznalo = input("Kő (k), papír (p) vagy olló (o)? ")

    l_betu = ["k", "p", "o"]
    gep_szam = r.choice(l_betu)

    #bolondbiztosítás
    if felhasznalo not in l_betu:
        print("Helytelen formátum! Nem tudsz olvasni?")
        continue

    #Kő
    print(f"Gép: {gep_szam}")
    if felhasznalo == "k" and gep_szam == "k":
        print("Döntetlen")
    elif felhasznalo == "k" and gep_szam == "p":
        print("Vesztettél!")
        gep_pont +=1
    elif felhasznalo == "k" and gep_szam == "o":
        print("Nyertél!")
        fh_pont += 1

    #Papír
    if felhasznalo == "p" and gep_szam == "k":
        print("Nyertél!")
        fh_pont += 1
    elif felhasznalo == "p" and gep_szam == "p":
        print("Döntetlen!")
    elif felhasznalo == "p" and gep_szam == "o":
        print("Vesztettél")
        gep_pont +=1

    #Olló
    if felhasznalo == "o" and gep_szam == "k":
        print("Vesztettél!")
        gep_pont +=1
    elif felhasznalo == "o" and gep_szam == "p":
        print("Nyertél!")
        fh_pont += 1
    elif felhasznalo == "o" and gep_szam == "o":
        print("Döntetlen!")

    print(f"Felhasználó: {fh_pont}")
    print(f"Gép: {gep_pont}")

    #Kívánja-e folytatni a felhasználó
    felhasznalo_folytatja = input("Folytatod a játékot? i/n ")
    if felhasznalo_folytatja != "i" and felhasznalo_folytatja != "n":
        print("Helytelen formátum! i/n A JÁTÉK ÚJRAKEZDŐDIK!")
        continue
    elif felhasznalo_folytatja == "n":
        break