RandomNumber = 75

"""userInput = int(input("Entrez un nombre au hazard..."))
print(userInput)
if userInput > RandomNumber:
    print("Vous etes trop loin du nombre (plus)")
elif userInput < RandomNumber:
    print("Vous n'y etes pas encore(moins)")
elif userInput == userInput:
    print(f"Génial vous avez trouvé le nombre est{RandomNumber}")
    print("fin du programm...")"""

MaxTry = 3
i = 0
while i < MaxTry:
    userInput = int(input("Entrez un nombre au hazard:"))
    if userInput == RandomNumber:
                print(f"Génial vous avez trouvé. Le nombre es : {RandomNumber}")
                break
    elif userInput < RandomNumber:
            print(f"Vous n'y etes pas encore (moins)")
    elif userInput > RandomNumber:
        print(f"Vous etes trop loin du nombre (plus)")
    i += 1   
else: 
        print(f"Vous avez essayé {MaxTry} fois et vous avez échoué, wesh...pfff")   





