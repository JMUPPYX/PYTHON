
# Faire une compréhension de liste avec les 4 exemples

# # 1 EXO ON RECUP UNIQUEMENT LES NOMBRE PAIR
# nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
# # LISTE VIDE
# nombres_pairs = []
# # on boucle sur tous les nombres
# for i in nombres:
#     # si le modulo de chauqe nombre est == 0
#     if i % 2 == 0 :
#         # on ajoute ce nombre à la liste nombre_pairs
#         nombres_pairs.append(i)
#         print(nombres_pairs)

# exo 1 comprehension de liste
nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
# on recup la valeur de i pour i dans nombres si i modulo de 2 est égal à 0
nombres_pairs = [i for i in nombres if i % 2 == 0]
print(nombres_pairs)



# exo 2 on veut afficher les nombres de -10 à 10
# nombres = range(-10, 10)
# # LISTE VIDE
# nombres_positifs = []
# # on boucle sur tous les nombres
# for i in nombres:
#     # si element est inf ou == à 0
#     if i >= 0:
#         # on ajoute ce nombre à la liste nombre_positif
#         nombres_positifs.append(i)

# print(nombres_positifs)


# exo 2 comprehension de liste
nombres = range(-10, 10)
# on recup la valeur de i pour i dans nombres si i et sup ou égal à 0
nombres_positifs = [i for i in nombres if i >= 0]
print(nombres_positifs)



# exo 3 on veut afficher 5 nombres et doubler chaque nombre de cette liste
# nombres = range(5)
# # LISTE VIDE
# nombres_doubles = []
# # on boucle sur tous les nombres
# for i in nombres:
#     # ajouter élément *2
#    nombres_doubles.append(i*2)
# print(nombres_doubles)

# exo 3 comprehension de liste
nombres = range(5)
# i * 2 pour i dans nombres
nombres_doubles = [i * 2 for i in nombres]
print(nombres_doubles)


# exo 4 on veut afficher 10 chiffres de 0-9
# nombres = range(10)
# # LISTE VIDE
# nombres_inverses = []
# # on boucle sur tous les nombres
# for i in nombres:
#    # si le modulo de chauqe nombre est == 0 = nombre pair on l'ajoute
#    if i % 2 == 0:
#     nombres_inverses.append(i)
#      # sinon en ajoute - au chiffre 
#    else: 
#        nombres_inverses.append(-i)

# print(nombres_inverses)

# exo 4 comprehension de liste avec un else
nombres = range(10)
# i si i module de 2 == 0 on retourne i sinon -i pour i dans nombres
nombres_inverses = [i if i % 2 == 0 else -i for i in nombres]
print(nombres_inverses)