from turtle import Turtle

SCREEN_POSITION = 'center'
FONT_STYLE = ("Courier", 15, "normal")


class Message(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=SCREEN_POSITION, font=FONT_STYLE)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=SCREEN_POSITION, font=FONT_STYLE)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
