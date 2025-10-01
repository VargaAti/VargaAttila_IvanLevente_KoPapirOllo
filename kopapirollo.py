import random as r

folytatja = True

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
        break

    #Kő
    print(f"Gép: {gep_szam}")
    if felhasznalo == "k" and gep_szam == "k":
        print("Döntetlen")
    elif felhasznalo == "k" and gep_szam == "p":
        print("Vesztettél!")
    elif felhasznalo == "k" and gep_szam == "o":
        print("Nyertél!")

    #Papír
    if felhasznalo == "p" and gep_szam == "k":
        print("Nyertél!")
    elif felhasznalo == "p" and gep_szam == "p":
        print("Döntetlen!")
    elif felhasznalo == "p" and gep_szam == "o":
        print("Vesztettél")

    #Olló
    if felhasznalo == "o" and gep_szam == "k":
        print("Vesztettél!")
    elif felhasznalo == "o" and gep_szam == "p":
        print("Nyertél!")
    elif felhasznalo == "o" and gep_szam == "o":
        print("Döntetlen!")

    #Kívánja-e folytatni a felhasználó
    felhasznalo_folytatja = input("Folytatod a játékot? i/n ")
    if felhasznalo_folytatja == "n":
        break
    elif felhasznalo_folytatja == "i":
        folytatja = True
    else:
        break