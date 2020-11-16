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


    while plateau[x + y * 3] != '0':
        print("La case est déjà joué ! Observe un peu ")
        x, y = coupHumain()

    plateau[x + y * 3] = joueur

    return plateau


def gagnant(plateau):
    for i in range(3):
        if plateau[3 * i + 0] == "O" and plateau[3 * i + 1] == "O" and plateau[3 * i + 2] == "O":
            return True, "Joueur 1"
        if plateau[3 * i + 0] == "X" and plateau[3 * i + 1] == "X" and plateau[3 * i + 2] == "X":
            return True, "Joueur 2"

    for i in range(3):
        if plateau[i] == "O" and plateau[i + 3] == "O" and plateau[i + 6] == "O":
            return True, "Joueur 1"
        if plateau[i] == "X" and plateau[i + 3] == "X" and plateau[i + 6] == "X":
            return True, "Joueur 2"

    if plateau[0] == "O" and plateau[4] == "O" and plateau[8] == "O":
        return True, "Joueur 1"
    if plateau[0] == "X" and plateau[4] == "X" and plateau[8] == "X":
        return True, "Joueur 2"

    if plateau[2] == "O" and plateau[4] == "O" and plateau[6] == "O":
        return True, "Joueur 1"
    if plateau[2] == "X" and plateau[4] == "X" and plateau[6] == "X":
        return True, "Joueur 2"

    return False, "Aucun"


def plateauPlein(plateau):
    for i in plateau:
        if i == '0':
            return False
    return True


def jouer(joueur1, joueur2, plateau):
    afficher_grille(plateau)

    for i in range(9):
        if i % 2 == 0:
            print("C'est au joueur 1 de joueur")
            plateau = placerCoupHumain(plateau, joueur1)
        else:
            print("C'est au joueur 2 de joueur")
            plateau = placerCoupHumain(plateau, joueur2)

        afficher_grille(plateau)

        if gagnant(plateau)[0]:
            print("Le gagnant est : ", gagnant(plateau)[1])
            break
        elif plateauPlein(plateau):
            print("Il y a égalité")
            break


jouer(j1, j2, liste)