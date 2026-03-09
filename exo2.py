list_de_nom = ["Alice", "Bob", "Charlie", "Diana"]

print("Liste des noms :", list_de_nom)
print("trier de maniere alphabetique :", sorted(list_de_nom))

list_de_nom.append("Eve")  # Ajout de plusieurs éléments à la fin de la liste,
print(sorted(list_de_nom))
list_de_nom.append("Frank")
list_de_nom.append("Grace")
print(sorted(list_de_nom))

#Tuple : c'est une liste qui ne peu etre modifiée apres sa création
mon_tuple = ("Rouge", "Vert", "Bleu")
print("Mon tuple :", mon_tuple)
# flag
print("------------Parcontre avec le tuple je peu faire un count-------------")
print (mon_tuple.count("Rouge")) 

# Un set c'est n conteneur ordonné, modifiable et non indexable

mon_set = {"Pomme", "Banane", "Cerise"}
print("Mon set :", mon_set)

# UN dictionnaire : c'est une collection non ordonnée, modifiable et indexée fonctionnant avec un système de clés valeurs

mon_dictionnaire = {
    "nom": "HOUNKPE-SAGBO",
    "prenom": "Steeven",
    "age": 20,
    "ville": "Nantes"
}

print("Mon dictionnaire :", mon_dictionnaire)
print("Mon prénom est :", mon_dictionnaire.keys()) # Affiche les clés du dictionnaire
print("Mon prénom est :", mon_dictionnaire.values()) # Affiche les valeurs du dictionnaire
print("Mon prénom est :", mon_dictionnaire.items()) # Affiche les paires clé-valeur du dictionnaire
print("Mon prénom est :", mon_dictionnaire.get("prenom")) # Affiche la valeur associée à la clé 'prenom'



