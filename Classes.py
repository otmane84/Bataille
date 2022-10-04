from random import*


class Carte:

    def __init__(self, hauteur, couleur):
        self.hauteur = hauteur
        self.couleur = couleur

    def afficher_carte(self):
        return str(self.hauteur)+self.couleur


class PaquetDeCartes:

    def __init__(self, mon_paquet):
        self.mon_paquet = mon_paquet

    def est_vide(self):
        if self.mon_paquet == []:
            return True
        else:
            return False

    def taille(self):
        return len(self.mon_paquet)

    def battre(self):
        shuffle(self.mon_paquet)

    def tirer_carte(self):
        if self.est_vide():
            return None
        else:
            carte = self.mon_paquet[0]
            self.mon_paquet.pop(0)
            return carte

    def ajouter_paquet(self, paquet):
        for carte in paquet:
            self.mon_paquet.append(carte)

    def afficher_paquet(self):
        for carte in self.mon_paquet:
            print(Carte.afficher_carte(carte))

    def paquet_liste(self):
        liste = []
        for carte in self.mon_paquet:
            liste.append(Carte.afficher_carte(carte))
        return liste
