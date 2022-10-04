from random import*
from Fonctions import*
from Classes import*
from Canstantes import*

print("\nAppuyer sur entrer pour commencer une nouvelle partie")
print("Appuyer sur la touche t ou T puis entrer pour reprendre la partie")
print("Appuyer sur la touche q ou Q puis entrer pour quiter le jeu")
reponse = input()
if reponse == 't' or reponse == 'T':
    main, paquet_1, paquet_2 = telecharger()
    A = PaquetDeCartes(paquet_1)
    B = PaquetDeCartes(paquet_2)
    print("\t\t\tOn reprend la partie")
elif reponse == 'q' or reponse == 'Q':
    exit()
else:
    shuffle(paquet)
    paquet_1 = []
    paquet_2 = []
    for i in range(26):
        paquet_1.append(paquet[i])
        paquet_2.append(paquet[i+26])
    A = PaquetDeCartes(paquet_1)
    B = PaquetDeCartes(paquet_2)
    PaquetDeCartes.battre(A)
    PaquetDeCartes.battre(B)
    main = 0
    print("\t\t\tDébut de la partie")


jouer(A, B, main)
