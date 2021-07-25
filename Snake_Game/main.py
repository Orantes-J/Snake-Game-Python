import time
from food import Food
from turtle import Screen
from snake import Snake
from game_title import Message

# import time
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My snake game")
# screen.tracer(0)
#
# cords = [(0, 0), (-20, 0), (-40, 0)]
#
# squares = []
#
# for i in range(3):
#     new_square = Turtle(shape='square')
#     new_square.color('white')
#     new_square.penup()
#     new_square.goto(cords[i])
#     squares.append(new_square)
#
#
# game_is_on = True
#
# while game_is_on:
#     screen.update()
#     time.sleep(1)
#
#     for square_num in range(len(squares)-1, 0, -1):
#         new_x = squares[square_num - 1].xcor()
#         new_y = squares[square_num - 1].ycor()
#
# screen.exitonclick()

screen_message = Message()
snake = Snake()
food = Food()


screen = Screen()
screen.title('My snake game')
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True

while game_is_on:

    my_score = 0

    screen.update()
    time.sleep(0.1)

    snake.move()

    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')
    screen.onkey(snake.exit, 'space')

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        screen_message.increase_score()

    # collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        game_is_on = False
        screen_message.game_over()

    # collision with itself
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            print("Processing second validation")
            game_is_on = False
            screen_message.game_over()

screen.exitonclick()
