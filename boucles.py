'''
UserAge = (input("Entrez votre age : ")) # Demander a l'utilisateur son age

if int(UserAge) < 18: # Verifier si l'age est inferieur a 18
    print("Vous etes mineur") 
elif int(UserAge) == 18: # Verifier si l'age est egal a 18
    print("Vous etes tout juste majeur")    
else:
    print("Vous etes majeur")
    if UserAge in ["21", "30", "40", "50", "60"]: # Verifier si l'age est dans la liste des ages importants
        print("Vous etes dans une decennie importante de votre vie !")


# les opérateurs ternaires
status = "majeur" if UserAge >= 18 else "mineur"
print(f"Vous etes {status}.")
'''

# la boucle while
i = 0
while i < 5:
    print(i)
    i += 1

# la boucle for
list_Etudiants = ["Alice", "Bob", "Charlie", "Diana"]
for i in list_Etudiants:
    print(i)

# boucle for avec range
for i in range(5):
    print(i)

# Entrer utilisateur 
value = ("Entrez quelque chose :")
print(value)