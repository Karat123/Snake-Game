from turtle import Turtle, Screen

screen = Screen()
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.show_score()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.show_score()


    def show_score(self):
        self.write(f"Score:{self.score} ", align="center", font=('open-sans-bold', 14, 'bold'))

    def update_score(self):
        self.clear()
        self.score += 1
        self.show_score()

    #def reset_score(self):


    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align="center", font=('open-sans-bold', 25, 'bold'))
        self.re_run = screen.textinput("Play Game Y/N)", "Do you want to play again ?")
        if self.re_run == "Y" or "y":
            re_run = True
        elif self.re_run == "N" or "n":
            re_run = False

