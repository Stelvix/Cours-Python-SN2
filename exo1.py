num1 = 20
num2 = 3
num3 = num1 * num2
num4 = num1 / num2
result = round(num3 + num4 - 11.111, 2)

# Afficher les deux nombres apres la virgule
print(f"Le résultat est : {result:.2f}")

print("la variable num1 est :", num1)
print("la variable num2 est :", num2)
print("la variable num3 est :", num3)
print("la variable num4 est :", num4)

print("le résultat final est :", result)


hello = "Hello world! , un classic quoi!"

print(hello[-2])

print("Mou" + 3 * "ha")

print(hello[:]) # Affricher toute la chaine

print(hello[10:]) # Afficher à partir du 10eme caractere jusqu'à la fin

print(hello[:10]) # Afficher du debut jusqu'au 10eme caractere

print(hello[-4:]) # Afficher les 4 derniers caracteres

print(hello[:-4]) # Afficher du debut jusqu'aux 4 derniers caracteres

print(hello[::]) # Afficher toute la chaine

print(hello[::2]) # Afficher toute la chaine en sautant un caractere sur deux

surnom = "Titi"
Age = 25

print(f"Bonjour je m'appel {surnom} et j'ai {Age} ans.") # Utilisation des f-strings pour l'affichage

ma_liste_pour_tout = [num1, num2, Age, "Nantes", ["Football", "Lecture", "Voyage"], hello, result, "json", 42.42, True, "react", ]
print("Voici ma liste pour tout :", ma_liste_pour_tout[2])

# Ajouter un élément à la liste
ma_liste_pour_tout.append("Bof hein") # Ajout d'un élément à la fin de la liste
print("Liste après ajout d'un élément :", ma_liste_pour_tout)   # Afficher la liste après l'ajout  
ma_liste_pour_tout.append(99) # Ajout d'un autre élément à la fin de la liste
print("Liste après ajout d'un élément :", ma_liste_pour_tout)
# Supprimer un élément de la liste
ma_liste_pour_tout.remove("json")
print("Liste après suppression d'un élément :", ma_liste_pour_tout)

ma_liste_pour_tout.clear() # Vider la liste
print("Liste après avoir été vidée :", ma_liste_pour_tout)

ma_liste_pour_tout.append("On essaye quelque chose de nouveau")
print("Nouvelle liste :", ma_liste_pour_tout)
