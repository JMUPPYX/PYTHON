import os

chemin = "/Users/famil/Desktop/Formation dev/Python"
dossier = os.path.join(chemin, "dossier","test")
print(dossier)
# if not os.path.exists(dossier):
#     os.makedirs(dossier)
if  os.path.exists(dossier):
    os.removedirs(dossier)