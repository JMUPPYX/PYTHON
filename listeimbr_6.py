# liste imbriqués - on récupère l'éléments de notre liste avec son indice et on utilise les slices
liste = ["Python", ["Java","C#",["C"]],["Ruby"]]

# on veut récup Java
# print (liste[1][0])

# on veut récup C
# print(liste[1][2])

# # on veut récup la chaine de caractère C
# print(liste[1][2][0])

# on veut récup une ou plrsr lettre
# print(liste[0][0])

# on veut récup une ou plrsr lettre
print(liste[0][0:2])