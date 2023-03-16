class Karaoke:
    def __init__(self):
        self.joueurs = []
        self.musiques = ["knocking at heaven's door", "con te partiro", "Ces gens là "]

    def showMusiques(self):
        for i in range(len(self.musiques)):
            print(str(self.musiques[i]) + " > " + str(i))

    def suppJoueur(self):
        if len(self.joueurs) > 1:
            for i in range(len(self.joueurs)):
                print(str(self.joueurs[i].pseudo) + " > " + str(i))
            choix = int(input("Quel joueur voulez vous supprimer ? "))
        else:
            print("il doit y avoir plusieurs joueurs pour en supprimer un.")

# incapable de faire le reste... 