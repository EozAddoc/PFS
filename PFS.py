import random

player1 = input("Entrez votre nom: ")
player2 = "Joueur IA"

player1Wins = 0
player2Wins = 0
startGame = True


while startGame:
    try:
        choice = int(input("Choisissez Pierre (1), Feuille (2) ou Ciseaux (3): "))
        if choice not in [1, 2, 3]:
            print("Choix invalide, veuillez entrer 1, 2 ou 3.")
            continue
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        continue
    
    AIchoice = random.randint(1, 3)


    if AIchoice == 1 and choice == 3:
        print(f"{player2} a gagné avec Pierre contre Ciseaux.")
        player2Wins += 1
    elif AIchoice == 2 and choice == 1:
        print(f"{player2} a gagné avec Feuille contre Pierre.")
        player2Wins += 1
    elif AIchoice == 3 and choice == 2:
        print(f"{player2} a gagné avec Ciseaux contre Feuille.")
        player2Wins += 1
    elif AIchoice == choice:
        print("Égalité!")
    elif choice == 1 and AIchoice == 3:
        print(f"{player1} a gagné avec Pierre contre Ciseaux.")
        player1Wins += 1
    elif choice == 2 and AIchoice == 1:
        print(f"{player1} a gagné avec Feuille contre Pierre.")
        player1Wins += 1
    elif choice == 3 and AIchoice == 2:
        print(f"{player1} a gagné avec Ciseaux contre Feuille.")
        player1Wins += 1

    if player1Wins >= 3 or player2Wins >= 3:
        startGame = False
        if player1Wins > player2Wins:
            print(f"\n{player1} a gagné")
        else:
            print(f"\n{player2} a gagné")
