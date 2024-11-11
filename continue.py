# continue va executer le script tant que la condtion est remplie et affichera les chaine de caractères
liste = ["1","4","25","Paul","3","Pierre"]
for element in liste:
    if element.isdigit():
        continue
print(element)