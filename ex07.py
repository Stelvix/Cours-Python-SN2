passArechercher = "pwd"

fichier = open("index.html", "r")
if fichier is None:
    print("Le fichier n'existe pas")
else:
    print(f"le fichier existe du coup...{fichier} contient bien le mot de pass")
    for ligne in fichier:
        if passArechercher in ligne:
            print(ligne)
