
import socket
import os

target = "linkedin.com"
ip = socket.gethostbyname(target)

print(f"l'IP de {target} est {ip}")

num1 = 20
num2 = 3
num3 = num1 + num2
num4 = num1 / num2
my_name = "Steeven"
age = 21

ma_liste_de_course = ["couscous", "pomme", "orange"]

ma_liste_de_course.append(["Bof", "patate","Bat"])

print(f"Ma nouvelle liste{ma_liste_de_course}")

 
def greet(name):
    return f"Hello, {name}!"
print(greet("Steeven"))

with open("tryFileHandling.txt", "w") as file:
    file.write("Python makes file handling easy!")


""" print(my_name[0:5])

print(f"Résultat de Num1: {num1}")
print(f"Résultat de Num2: {num2}")
print(f"Résultat de Num3: {num3}")
print(f"Résultat de Num4: {round(num4, 5)}")

print(type(num1))

my_string = "Mou" + 3 * "ha"
print(my_string) """
