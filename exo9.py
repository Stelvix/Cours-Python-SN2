import os.path
"""directory = os.path.exists("photos")

if os.path.exists(directory):
    print(f"Le repertoire {directory} existe bien")"""

currentdir = os.getcwd()
print(f"Vous etes dans : {currentdir}")

searchedFile = "photos"

entries = os.listdir(currentdir)
for Dossier in entries:
        if searchedFile in Dossier:
            print(f"Dossier {searchedFile} trouvé")
            os.rename('jpeg', 'jpg')
            print("Les extensions des fichiers on bien été changés")
        else: 
            print(f"Dossier {searchedFile} non trouvé")
            