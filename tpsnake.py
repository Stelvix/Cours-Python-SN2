import turtle as t
import random 
import time
#screen
screen = t.Screen()
screen.bgcolor("white")
screen.setup(600, 600)
delay = 0.1

segment = []
score = 0
highScrore = 0
Colision = True

# serpent
snake = t.Turtle()
snake.shape("square")
snake.color("orange")
snake.penup()
snake.goto(0, 100)
snake.direction = "stop"


# food of the snake
food = t.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, 100)

# affichage du scrore
textScore = t.Turtle()
textScore.penup()
textScore.speed(0)
textScore.goto(0, 250)
textScore.hideturtle()
textScore.write("Score: 0 High Score: 0", align="center", font=("verdana", 30, "normal"))

looseScore = t.Turtle()
looseScore.penup()
looseScore.speed(0)
looseScore.goto(0, 100)
looseScore.hideturtle()
looseScore.write("State", font=("Candara", 30, "normal"), align=("center"))


# Fonction pour le mouvement
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

#directions functions
def go_up():
    snake.direction = "up"
def go_down():
    snake.direction = "down"
def go_left():
    snake.direction = "left"
def go_right():
    snake.direction = "right"


screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Bouble principale pour le jeu


while True:
    screen.update() # mettre à jour le screen
    move() # ici on appel la fonction move pour déplacer le serpene qu'on a crée
    time.sleep(delay) # on appel la variable delay qu'on a créé en haut grace à l'import de time en faut

# On s'assure que le serpent ne sort pas du screen
    if snake.xcor() > 280 or snake.xcor() < -280 or snake.ycor() > 280 or snake.ycor() < -280:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "stop"
        

    # Réinitialiser les segments
        for seg in segment:
            seg.goto(1000, 1000)
        segment.clear()

        score = 0 
        textScore.clear()
        textScore.write("Score: {}  High Score: {}".format(score, highScrore),
                    align="center", font=("Arial", 20, "normal"))
        if score == 0:
            looseScore.write("Perdu") 


    # Manger la nourriture an faire grandire le serpent
    if snake.distance(food) < 20:
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        food.penup()
        food.goto(x, y)
        food.pendown()
# augmenter la taille du serpent
        newSeg = t.Turtle()
        newSeg.shape("square")
        newSeg.color("grey")
        newSeg.penup()
        segment.append(newSeg)
    
        score += 1

    if score > highScrore:
            highScrore = score
            textScore.clear()
            textScore.write("Score: {}  High Score: {}".format(score, highScrore), align="center", font=("Arial", 30, "normal"))

    for i in range(len(segment) - 1, 0, -1):
        x = segment[i - 1].xcor()
        y = segment[i - 1].ycor()
        segment[i].goto(x, y)

    # Move the first segment to follow the head
    if len(segment) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segment[0].goto(x, y)

    

