# joueur1 = input("Saissisez le nom du joueur 1 :")
# joueur2 = input("Saissisez le nom du joueur 2 :")

j1 = 'X'
j2 = 'O'

liste = ["0", "0", "0", "0", "0", "0", "0", "0", "0"]


def afficher_grille(grille):
    print("     0)  1)  2)")
    print("   -------------")
    print("0)", end='')
    for i in range(3):
        print(" |  " + str(grille[i]), end='')
    print(" |")
    print("   -------------")
    print("1)", end='')
    for i in range(3):
        print(" |  " + str(grille[i + 3]), end='')
    print(" |")
    print("   -------------")
    print("2)", end='')
    for i in range(3):
        print(" |  " + str(grille[i + 6]), end='')
    print(" |")
    print("   -------------")


def coupHumain():
    x = input("coordonnée x : ")
    y = input("coordonnée y : ")

    while int(x) > 2 or int(x) < 0:
        x = input("coordonnée x : ")

    while int(y) > 2 or int(y) < 0:
        y = input("coordonnée y : ")

    return int(x), int(y)


def placerCoupHumain(plateau, joueur):
    x, y = coupHumain()

    plateau[x + y * 3] = joueur

    return plateau


def gagnant(plateau):
    if plateau[0] == "0" and plateau[1] == "0" and plateau[2] == "0":
        return True



liste = placerCoupHumain(liste, j1)
afficher_grille(liste)
