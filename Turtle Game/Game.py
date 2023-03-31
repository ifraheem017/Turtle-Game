
# working on game level selection in line no 37...
import turtle
import random
import time

# global Variables
game = True
c_sec = time.localtime().tm_sec
speed = 1.5
obt_Scor = 0.0
c_down = 60
Level = 1
game_seconds = 0

# creating Display Screen for game.
turtle.hideturtle()
s = turtle.getscreen()
s.bgcolor('orange')
name = s.textinput("Login", "Enter you Name here...")
s.title(name)
s.screensize(200, 200)
width = 630
height = 630
s.setup(width, height)
owner = turtle.Turtle()
owner.penup()
owner.ht()
owner.goto(-35, 270)
dev_owner = turtle.Turtle()
dev_owner.ht()
dev_owner.penup()
dev_owner.goto(-210,0)
dev_owner.write(f"Developed By M Ifraheem", font=("Arial", 30, "normal"))
time.sleep(2)


# Level_Selection = turtle.Turtle()
# Level_Selection.ht()
# Level_Selection.penup()
# Level_Selection.write("Welcome to Game. Please Select Game Level...\n1. New Game\n2. Level 1\n")

dev_owner.clear()
owner.write("M IFRAHEEM",font=("Arial", 10, "normal"))

# creating border for screen
border = turtle.Turtle()
border.ht()
border.penup()
border.speed(200)
border.goto(300, 300)
border.pendown()
border.st
border.setheading(180)
border.fd(600)
border.setheading(270)
border.fd(600)
border.setheading(360)
border.fd(600)
border.setheading(90)
border.fd(600)

# creating Snake on Screen.
snake = turtle.Turtle()
snake.penup()
snake.shape('turtle')
snake.color('purple')

# Creating game score bord
score = turtle.Turtle()
score.ht()
score.penup()
score.goto(-250, 250)

# level final score bord
score_bord = turtle.Turtle()
score_bord.ht()
score_bord.penup()
score_bord.goto(-150, 0)

# Food for snake
food = turtle.Turtle()
food.shape('circle')
food.penup()
food.shapesize(0.5, 0.5, 0.5)
x = random.randint(-295, 295)
y = random.randint(-295, 295)
food.goto(x, y)
write_score = score.write(
    f"  Score : {obt_Scor}\t\t\tLevel : {Level} / 4\t\t\tTime Left : {c_down}", font=("Arial", 10, "normal"))

# controlling the movement of snake
def movement():
    s.listen()
    s.onkey(lambda: snake.setheading(90), 'Up')
    s.onkey(lambda: snake.setheading(180), 'Left')
    s.onkey(lambda: snake.setheading(360), 'Right')
    s.onkey(lambda: snake.setheading(270), 'Down')

# game over function
# if snake go out of range then must come back


def turtle_back(t):
    if t.xcor() >= 295:
        t.ht()
        t.setx(-295)
        t.st()

    elif t.xcor() < -295:
        t.ht()
        t.setx(295)
        t.st()

    elif t.ycor() > 295:
        t.ht()
        t.sety(-295)
        t.st()

    elif t.ycor() < -295:
        t.ht()
        t.sety(295)
        t.st()


def game_over_snake_outside():
    if snake.xcor() >= 292:
        game_over()

    elif snake.xcor() < -292:
        game_over()

    elif snake.ycor() > 292:
        game_over()

    elif snake.ycor() < -292:
        game_over()


def snake_Level():
    if Level == 1:
        turtle_back(snake)

    elif Level == 2:
        game_over_snake_outside()


def catch_snake():
    global speed, obt_Scor, c_down
    if snake.distance(food) < 10:
        food.ht()
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        food.st()
        speed += 0.3
        score.clear()
        obt_Scor += 5
        write_score = score.write(
            f"  Score : {obt_Scor}\t\t\tLevel : {Level} / 4\t\t\tTime Left : {c_down}", font=("Arial", 10, "normal"))

# count down


def cont_down():
    global c_sec, c_down, write_score
    if c_sec != time.localtime().tm_sec:
        score.clear()
        c_down -= 1
        write_score = score.write(
            f"  Score : {obt_Scor}\t\t\tLevel : {Level} / 4\t\t\tTime Left : {c_down}", font=("Arial", 10, "normal"))
        c_sec = time.localtime().tm_sec


"""-----------Level 02-----------"""

lft = turtle.Turtle('square')
right = turtle.Turtle('square')
up = turtle.Turtle('square')
down = turtle.Turtle('square')


def hide_wall():
    lft.ht()
    up.ht()
    down.ht()
    right.ht()

hide_wall()

def create_border():
    # creating left border
    lft.penup()
    lft.shapesize(30, 0.5, 0.5)
    lx = -300
    lft.goto(lx, 0)

    # right border
    right.penup()
    right.shapesize(30, 0.5, 0.5)
    rx = 300
    right.goto(rx, 0)

    # Upper border
    up.penup()
    up.shapesize(0.5, 30, 0.5)
    uy = 300
    up.goto(0, uy)

    # bottom border
    down.penup()
    down.shapesize(0.5, 30, 0.5)
    dy = -300
    down.goto(0, dy)

    lft.st()
    right.st()
    up.st()
    down.st()


def game_over():
    snake.ht()
    food.ht()
    score_bord.write(f"    Game Over...!\n Your Score is : {obt_Scor}", font=(
        "Arial", 30, "normal"))
    time.sleep(3)
    exit()


"""-----------------Level 03-----------------"""

bot = turtle.Turtle('turtle')
bot.ht()
bot.penup()
bot2 = turtle.Turtle('turtle')
bot2.ht()
bot2.penup()
bot2.setheading(180)

angle_time = 0
while Level <= 2:
    write_score
    snake.fd(speed)
    movement()
    catch_snake()
    snake_Level()
    cont_down()

    if c_down == game_seconds:
        snake.ht()
        food.ht()
        score_bord.write(f"      Time Up...!\n Your Score is : {obt_Scor}\n     Next Level...!", font=(
            "Arial", 30, "normal"))
        time.sleep(3)
        score_bord.clear()
        snake.st()
        food.st()
        snake.home()
        Level = Level + 1
        create_border()
        speed = 2.5
        c_down = 60

def bot_catch():
    if snake.distance(bot) < 20 or snake.distance(bot2) < 20:
        game_over()

snake.goto(0, -200)
bot.goto(50, 0)
bot2.goto(-50, 50)
snake.setheading(90)
n = 1
speed = 5
c_down = 60
hide_wall()
while Level == 3:
    write_score
    snake.fd(speed)
    bot.st()
    bot2.st()
    bot.fd(1)
    bot2.fd(1)
    movement()
    catch_snake()
    cont_down()
    if c_down == game_seconds:
        snake.ht()
        food.ht()
        score_bord.write(f"      Time Up...!\n Your Score is : {obt_Scor}\n     Next Level...!", font=(
            "Arial", 30, "normal"))
        time.sleep(3)
        score_bord.clear()
        snake.st()
        food.st()
        snake.home()
        Level = Level + 1
    turtle_back(snake)
    turtle_back(bot)
    turtle_back(bot2)
    bot_catch()

    if n % 100 == 0:
        bot.setheading(random.randint(0, 180))
        bot2.setheading(random.randint(180, 360))
    n += 1

"""-------------------Level 04------------------"""
abstacles = turtle.Turtle('square')
abstacles.shapesize(3, 3, 3)
snake.goto(0, -200)
snake.setheading(90)


def bot_wall(t):
    if t.xcor() >= 295:
        t.setheading(180)

    elif t.xcor() < -295:
        t.setheading(360)

    elif t.ycor() > 295:
        t.setheading(270)

    elif t.ycor() < -295:
        t.setheading(90)


create_border()
speed = 6
c_down = 60
while Level == 4:
    write_score
    snake.fd(speed)
    bot.st()
    bot2.st()
    bot.fd(1)
    bot2.fd(1)
    bot_wall(bot)
    bot_wall(bot2)
    movement()
    catch_snake()
    cont_down()
    bot_catch()
    if abstacles.distance(snake) < 50:
        abstacles.ht()
        game_over()

    game_over_snake_outside()
    if c_down == game_seconds:
        snake.ht()
        food.ht()
        score_bord.write(f"      Time Up...!\n Your Score is : {obt_Scor}\n     Next Level...!", font=(
            "Arial", 30, "normal"))
        time.sleep(3)
        score_bord.clear()
        snake.st()
        food.st()
        snake.home()
        Level = Level + 1
        c_down = 60


# while Level == 5:
#     write_score
#     snake.fd(speed)
#     bot.st()
#     bot2.st()
#     bot.fd(1)
#     bot2.fd(1)
#     movement()
#     catch_snake()
#     cont_down()
#     bot_catch()
turtle.mainloop()
