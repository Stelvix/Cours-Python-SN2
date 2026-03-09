import turtle
# initialisation
window = turtle.Screen()
window.title("Ma premier fenètre")
window.bgcolor("green")
window.setup(600, 400)

#Création d'une curseur turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.speed(5)

# faire un cercle
t.color("white")
t.circle(200)
t.teleport(78, 23)
# faire un cercle
t.color("violet")
t.circle(100)

# faire un cercle
t.color("orange")
t.circle(90)

# faire un cercle
t.color("red")
t.circle(80)

# faire un cercle
t.color("white")
t.circle(70)

# faire un cercle
t.color("yellow")
t.circle(60)

# faire un cercle
t.color("blue")
t.circle(50)

# faire un cercle
t.color("purple")
t.circle(40)

# faire un cercle
t.color("black")
t.circle(30)

# faire un cercle
t.color("cyan")
t.circle(20)
turtle.done()