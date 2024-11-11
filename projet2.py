# projet2 calculatrice
# definit nos varibales a et b vide car se sera les entrer de notre utilisateur
a = ""
b = ""
# tant que a et b ne sont pas des nombres on va boucler et afficher notre print if et nos deux input
while not (a.isdigit() and b.isdigit()):
    # avec la fonction input on demande à l'utilisateur d'entrer des nombres
    a = input("Entrez un premier nombre :")
    b = input ("Entrez un deuxième nombre :")
    # si a et b ne contiennent pas un nombre
    if not (a.isdigit() and b.isdigit()):
    # on affiche notre print
        print("Veuillez entrer deux nombres valides")

print (f"Le resultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")

# on peut supprimer la igne 11 cela fonctionne aussi