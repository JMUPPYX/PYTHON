mdp = input("Entrez votre mot de passe (min 8 caractères) : ")
mdp_trop_court = "Votre mot de passe est trop court."

# si la longueur du mdp est == à 0
if len(mdp) == 0 :
    # affiche en lettre majuscule la variable
    print(mdp_trop_court.upper())
    # sinon si la longueur du mdp est inf à 8 caractères
elif len(mdp) < 8:
    # affichela variable avec une lettre maj
    print(mdp_trop_court.capitalize())
    # sinon si le mdp nen contient que des nombre 
elif mdp.isdigit():
    print("votre mode passe ne contient que des nombres")
    # si aucune des condtions n'est verifiée
else :
    print ("Inscription terminée")
