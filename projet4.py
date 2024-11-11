# le nombre mystere

# on importe la fonction randing depuis le module random
from random import randint

# choix d un nombre aléatoire avec randint de 0 à 100
number_to_find = randint (0,100)
# nombre d'essai
remaining_attemps = 5

print("** Le jeu mystère**")

# boucle pple
# tant que l'essai est sup à 0
while remaining_attemps > 0 :
    # affiche le nombre d'essai             / permet de mettre le mot au pluriel si l'essai est sup à 1
    print(f"Il te reste {remaining_attemps} essai{'s'if remaining_attemps > 1 else ''}")

    # on recup la saisie du user saisie du userle nombre :")
    user_choice = input("Devine le nombre : ")
    # si le choix du user n'est pas un nombre
    if not user_choice.isdigit():
        # affiche
        print("Veuillez entrer un nombre valide.")
        # va passer tout ce qu'il y a après et revenir à la boulce while
        continue
    # si c'est bien un nombre la fonction int va convertir la chaine de caractère en nombre 
    # pyhton ne put comparer une chaine de caractère et un nombre
    user_choice = int(user_choice)

    if number_to_find > user_choice:
        print(f"Le nombre mystère est plus grand que {user_choice}")
    elif number_to_find < user_choice :
         print(f"Le nombre mystère est plus petit que {user_choice}")
        #  si le nombre est égal 
    else:
        # on sort de la boulce
        break
# on decremente le nombre d'essai
    remaining_attemps = remaining_attemps - 1

    # gagné ou perdu
    # si l'essai est égal à 0
if remaining_attemps == 0:
    #  on affiche
    print (f"Dommage ! Le nombre mysère était {number_to_find}")
else:
    print(f"Bravo! le nombre était bien {number_to_find}")
    # 6 - le nombre d'essai
    print(f"Tu as trouvé le nombre en {6 -remaining_attemps} essai")
    
print("Fin du jeu")