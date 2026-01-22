import turtle
import random
import time

delay = 0.1

scr = 0
high_scr = 0

window = turtle.Screen()
window.title("Snakesssss")
window.bgcolor("black")
window.setup(width=1000, height=700)
window.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, -30)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(-385, 280)
score.write("Score: 0 \nHigh Score: 0", align="center", font=("Courier", 20, "normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)


def restart_game():
    global scr, game_over
    for segment in segments:
        segment.hideturtle()
    segments.clear()
    head.goto(0, 0)
    head.direction = "stop"
    scr = 0
    score.clear()
    score.goto(-385, 280)
    score.write(
        "Score: 0 \nHigh Score: {}".format(high_scr),
        align="center",
        font=("Courier", 20, "normal"),
    )
    food.goto(0, 100)
    game_over = False


window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")
window.onkeypress(restart_game, "r")

game_over = False

while True:
    window.update()

    if not game_over:
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

        if len(segments) > 0:
            segments[0].goto(head.xcor(), head.ycor())

        move()

        if head.distance(food) < 20:
            food.goto(random.randint(-480, 480), random.randint(-330, 330))

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("green")
            new_segment.penup()
            segments.append(new_segment)

            scr += 1
            if scr > high_scr:
                high_scr = scr

            score.clear()
            score.goto(-485, 280)
            score.write(
                "Score: {}\nHigh Score: {}".format(scr, high_scr),
                align="left",
                font=("Courier", 20, "normal"),
            )

        if (
            head.xcor() > 490
            or head.xcor() < -490
            or head.ycor() > 340
            or head.ycor() < -340
        ):
            game_over = True
            score.clear()
            score.goto(0, 0)
            time.sleep(0.5)
            score.write(
                "Game Over! Press R to Restart",
                align="center",
                font=("Courier", 32, "bold"),
            )

        for segment in segments:
            if head.distance(segment) < 20:
                game_over = True
                score.clear()
                score.goto(0, 0)
                time.sleep(1)
                score.write(
                    "Game Over! Press R to Restart",
                    align="center",
                    font=("Courier", 32, "bold"),
                )
                break

    time.sleep(delay)
