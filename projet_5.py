# jeu de rôle

# on import le module random pour utiliser la fonction randint()
import random

ENEMY_HEALTH = 50
PLAYER_HEALTH = 50
NUMBER_OF_POTIONS = 3
# passe le tour ou non (lorsque le joueur prend une potion)
SKIP_TURN = False

# Tant que la boucle est vraie (infinie)
while True:
    # jeu du joueur
    # si le joueur passe son tour
    if SKIP_TURN:
        # affiche
        print("Vous passez votre tour...")
        # et on reinitilase la variable à False
        SKIP_TURN = False
    else:
        # la variable est vide car user n'a pas fait de choix
        user_choice = ""
        # tant que le choix du user n'est pas 1 ou 2 
        while user_choice not in ["1", "2"]:
            # affiche
            user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?")
        # si le choix est 1 attaque
        if user_choice == "1":
            # la variable va contenir le chiffre aléatoire de l'attaque
            your_attack = random.randint(5, 10)
            # correspond à la soustraction de l'attaque aux points de vie de l ennemi
            ENEMY_HEALTH = ENEMY_HEALTH - your_attack
            print(f"Vous avez infligé {your_attack} points de dégats à l'ennemi")
        # choix de la potion
        elif user_choice =="2":
            # si le nombre de potion est sup à 0
            if NUMBER_OF_POTIONS > 0:
                # on recupere des vies avec un nombre aléatoires
                potion_health = random.randint(15, 50)
                # on rajoute les point à la vie du joueur
                PLAYER_HEALTH = PLAYER_HEALTH + potion_health
                # on decremente le nombre de potion
                NUMBER_OF_POTIONS = NUMBER_OF_POTIONS - 1
                # quand on prend une potion on passe notre tour donc on le passe à True
                SKIP_TURN = True
                print(f"Vous récuperez {potion_health} point de vie et {NUMBER_OF_POTIONS} potions restantes")
            else:
                print("Vous n'avaez plus de potions...")
                # va nous permettre de repartir à la boucle
                continue

        # si l'ennemi est mort
        if ENEMY_HEALTH <= 0:
            print("Tu as gagné")
            break

        #  attaque de l ennemi
        # il a des point d attaque de 5 à 15
        enemy_attack = random.randint(5, 15)
        # on decremente les points de vie du joueur à celui de l'ennemi
        PLAYER_HEALTH = PLAYER_HEALTH - enemy_attack
        print(f"L'ennemi vous a infligé {enemy_attack} point de dégats")

        #  si la vie du joueur est inf ou = à 0
        if PLAYER_HEALTH <=0:
            print("Tu as perdu")
            break

        # stat
        print(f"Il vous reste {PLAYER_HEALTH} points de vie.")
        print(f"Il reste {ENEMY_HEALTH} points de vie à l'ennemi.")
        print("-"*50)

print("Fin du jeu")