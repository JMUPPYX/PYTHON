# la liste de courses
# les variables sont en majuscule car ce sont des variable globales car elles sont dans l'espace globales du script

# module sys permet de sortir du script dans le cas du choix 5
import sys
# liste vide qui va contenir notre liste de courses
LISTE = []

MENU = """Choisissez parmis les 5 options suivantes :
1: Ajouter un élèment à la liste
2: Retirer un élèment à la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
👉 Votre choix : """

# Cette variable nous permet de verifier que l'utilisateur fait un choix existant
MENU_CHOICES = ["1" , "2" , "3" , "3" , "4" , "5" , "6"]

while True:
    # vide
    user_choice = ""
    # tant que user_choice n'est pas un choix de la variable menu_choices
    while user_choice not in MENU_CHOICES:
        # affiche le MENU
        user_choice = input(MENU)
        # si l'entrée n'est pas valide
        if user_choice not in MENU_CHOICES:
            # affiche :
            print("Veuillez entrer un choix valide...")

    # ajouter / append
    if user_choice == "1": 
        # item correspond à l'element ajouter
        item = input("Entrez le nom d'un élèment à ajouter à la liste de courses : ")
        LISTE.append(item)
        print(f"L'élèment {item} a bien été ajouté.")

    # retirer /remove
    elif user_choice == "2": 
        item = input("Entrez le nom d'un élèment à retirer à la liste de courses : ")
        # si l'element est dans la liste
        if item in LISTE:
            # supp l'element de la liste
            LISTE.remove(item)
            # affiche
            print(f"L'élèment {item} a bien été supprimer.")
        else:
            print(f"Cette élèment {item} n'est pas dans la liste.")

     # afficher les éléments de la liste print
    elif user_choice == "3": 
        # si la liste contient 1 element
        if LISTE:
            print(f"Voici le contenu de la liste :")
            # i prend la valeur de 1 à l itération cela nous permet de commencer avec l'indice 1 avec enumerate()
            # pour chaque element affiche la liste en commencant par l'indice 1
            for i, item in enumerate(LISTE, 1):
                print(f"{i}.{item}")
        else:
            print(f"Votre liste ne contient aucun élément.")

    # vider la liste / méthode clear
    elif user_choice == "4": 
        LISTE.clear()
        print("La liste a été vidée de son contenu.")

    # quitter
    elif user_choice == "5": 
       print("A bientôt")
    #    le module sys nous permet de sortir du script actuel
       sys.exit()

# affiche des ----- entre chaque itération de la boucle
    print("-" * 50)
        

