from msilib.schema import Class
from random import*
from Classes import*


def jouer_main(A, B, main):
    print("\nAppuyer sur entrer pour jouer une main")
    print("Appuyer sur q ou Q puis entrer pour sauvegarder et quiter la partie")
    reponse = input()
    if reponse == 'q' or reponse == 'Q':
        exit()
    paquet = []
    carte_A = PaquetDeCartes.tirer_carte(A)
    carte_B = PaquetDeCartes.tirer_carte(B)
    paquet.append(carte_A)
    paquet.append(carte_B)
    print("\nMain numéro : ", main)
    print("le joueur A a joué la carte : ", Carte.afficher_carte(carte_A))
    print("le joueur B a joué la carte : ", Carte.afficher_carte(carte_B))
    while carte_A.hauteur == carte_B.hauteur:
        print("Bataille")
        carte_A_cachee = PaquetDeCartes.tirer_carte(A)
        carte_B_cachee = PaquetDeCartes.tirer_carte(B)
        print("les deux joueurs ont joué une carte face cachée, puis")
        paquet.append(carte_A_cachee)
        paquet.append(carte_B_cachee)
        carte_A = PaquetDeCartes.tirer_carte(A)
        carte_B = PaquetDeCartes.tirer_carte(B)
        print("le joueur A a joué la carte : ", Carte.afficher_carte(carte_A))
        print("le joueur B a joué la carte : ", Carte.afficher_carte(carte_B))
    if carte_A.hauteur > carte_B.hauteur:
        PaquetDeCartes.ajouter_paquet(A, paquet)
        print("Le joueur A remporte cette main")
    else:
        PaquetDeCartes.ajouter_paquet(B, paquet)
        print("Le joueur B remporte cette main")


def jouer(A, B, main):
    main = main + 1
    while PaquetDeCartes.est_vide(A) is False and PaquetDeCartes.est_vide(B) is False:
        jouer_main(A, B, main)
        print("Score du joueur A : "+str(PaquetDeCartes.taille(A)))
        print("Score du joueur B : "+str(PaquetDeCartes.taille(B))+"\n")
        sauvegarder(main, A, B)
        main = main + 1
    if PaquetDeCartes.est_vide(A):
        print("Le joueur B a gagné")
    else:
        print("Le joueur A a gagné")


def sauvegarder(main, A, B):
    try:
        fichier = open('partie.txt', 'w')
    except Exception as e:
        print("Echec : l'erreur était" + str(e))
    else:
        fichier.write(str(main)+"\n")
        fichier.write(str(PaquetDeCartes.paquet_liste(A))+"\n")
        fichier.write(str(PaquetDeCartes.paquet_liste(B))+"\n")
        fichier.close()


def telecharger():
    try:
        fichier = open('partie.txt')
    except Exception as e:
        print("Echec : l'erreur était" + str(e))
    else:
        main = fichier.readline()
        paquet_A = fichier.readline()
        paquet_B = fichier.readline()
        fichier.close()
    main = int(main)
    paquet_A = conversion_string_to_liste_objet(paquet_A)
    paquet_B = conversion_string_to_liste_objet(paquet_B)
    return main, paquet_A, paquet_B


def conversion_string_to_liste_objet(chaine):
    liste = eval(chaine)
    liste_objet = conversion_liste_to_liste_objet(liste)
    return liste_objet


def conversion_liste_to_liste_objet(liste):
    liste_objet = []
    for i in range(len(liste)):
        hauteur, couleur = extraire(liste[i])
        carte = Carte(hauteur, couleur)
        liste_objet.append(carte)
    return liste_objet


def extraire(chaine):
    if chaine == '2T':
        hauteur = 2
        couleur = 'T'
    elif chaine == '3T':
        hauteur = 3
        couleur = 'T'
    elif chaine == '4T':
        hauteur = 4
        couleur = 'T'
    elif chaine == '5T':
        hauteur = 5
        couleur = 'T'
    elif chaine == '6T':
        hauteur = 6
        couleur = 'T'
    elif chaine == '7T':
        hauteur = 7
        couleur = 'T'
    elif chaine == '8T':
        hauteur = 8
        couleur = 'T'
    elif chaine == '9T':
        hauteur = 9
        couleur = 'T'
    elif chaine == '10T':
        hauteur = 10
        couleur = 'T'
    elif chaine == '11T':
        hauteur = 11
        couleur = 'T'
    elif chaine == '12T':
        hauteur = 12
        couleur = 'T'
    elif chaine == '13T':
        hauteur = 13
        couleur = 'T'
    elif chaine == '14T':
        hauteur = 14
        couleur = 'T'
    elif chaine == '2C':
        hauteur = 2
        couleur = 'C'
    elif chaine == '3C':
        hauteur = 3
        couleur = 'C'
    elif chaine == '4C':
        hauteur = 4
        couleur = 'C'
    elif chaine == '5C':
        hauteur = 5
        couleur = 'C'
    elif chaine == '6C':
        hauteur = 6
        couleur = 'C'
    elif chaine == '7C':
        hauteur = 7
        couleur = 'C'
    elif chaine == '8C':
        hauteur = 8
        couleur = 'C'
    elif chaine == '9C':
        hauteur = 9
        couleur = 'C'
    elif chaine == '10C':
        hauteur = 10
        couleur = 'C'
    elif chaine == '11C':
        hauteur = 11
        couleur = 'C'
    elif chaine == '12C':
        hauteur = 12
        couleur = 'C'
    elif chaine == '13C':
        hauteur = 13
        couleur = 'C'
    elif chaine == '14C':
        hauteur = 14
        couleur = 'C'
    elif chaine == '2P':
        hauteur = 2
        couleur = 'P'
    elif chaine == '3P':
        hauteur = 3
        couleur = 'P'
    elif chaine == '4P':
        hauteur = 4
        couleur = 'P'
    elif chaine == '5P':
        hauteur = 5
        couleur = 'P'
    elif chaine == '6P':
        hauteur = 6
        couleur = 'P'
    elif chaine == '7P':
        hauteur = 7
        couleur = 'P'
    elif chaine == '8P':
        hauteur = 8
        couleur = 'P'
    elif chaine == '9P':
        hauteur = 9
        couleur = 'P'
    elif chaine == '10P':
        hauteur = 10
        couleur = 'P'
    elif chaine == '11P':
        hauteur = 11
        couleur = 'P'
    elif chaine == '12P':
        hauteur = 12
        couleur = 'P'
    elif chaine == '13P':
        hauteur = 13
        couleur = 'P'
    elif chaine == '14P':
        hauteur = 14
        couleur = 'P'
    elif chaine == '2K':
        hauteur = 2
        couleur = 'K'
    elif chaine == '3K':
        hauteur = 3
        couleur = 'K'
    elif chaine == '4K':
        hauteur = 4
        couleur = 'K'
    elif chaine == '5K':
        hauteur = 5
        couleur = 'K'
    elif chaine == '6K':
        hauteur = 6
        couleur = 'K'
    elif chaine == '7K':
        hauteur = 7
        couleur = 'K'
    elif chaine == '8K':
        hauteur = 8
        couleur = 'K'
    elif chaine == '9K':
        hauteur = 9
        couleur = 'K'
    elif chaine == '10K':
        hauteur = 10
        couleur = 'K'
    elif chaine == '11K':
        hauteur = 11
        couleur = 'K'
    elif chaine == '12K':
        hauteur = 12
        couleur = 'K'
    elif chaine == '13K':
        hauteur = 13
        couleur = 'K'
    else:
        hauteur = 14
        couleur = 'K'
    return hauteur, couleur
