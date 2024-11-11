# break  va sortir de la boucle 
liste = ["1","4","25","Paul","3","Pierre"]
for element in liste:
    if element.isdigit():
        break
print(element)