import os.path
userInput = input("Entrez quelque chose: ")
print("Vous avez entré :", userInput)
fichierAecrire = 'Garba.txt'
os.path.exists(fichierAecrire)

if os.path.exists(fichierAecrire):
    print("Vous avez entré :", userInput)
    print('\n')
    print("Le fichier existe déjà, ajout du texte à la fin du fichier.")
    f = open(fichierAecrire, 'a')
    f.write('\n' + userInput)
    f.close()
    print(f"Le texte a été ajouté à la fin du fichier, {fichierAecrire}")
else:
    print("Le fichier n'existe pas, création du fichier et écriture du texte.")
    print('\n')
    f = open(fichierAecrire, 'w')
    f.write(userInput)
    f.close()
print(f"Le texte a été écrit dans le fichier, {fichierAecrire}")