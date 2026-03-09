#Exo 5
phrase = input("Entrez une phrase : ")
def CompterLeNombreDeCharactres(phrase):
       if not phrase:
           return 0
       return 1 + CompterLeNombreDeCharactres(phrase[1:])
print("Le nombre de charactres dans la phrase est de :", CompterLeNombreDeCharactres(phrase))

#Etape 2
def is_palindrome(phrase):
      if phrase == '' or len(phrase)==1:
            print(f"la phrase {phrase} es un palindrome")
            return True
      elif phrase[0] != phrase[-1]:
            print(f"la phrase {phrase} n'es pas un palindrome")
            return False
      is_palindrome(phrase[1:-1])


