from turtle import Turtle
ALIGNMENT = 'center'
FONTS = ('Arial', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())

        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'score:{self.score} High score: {self.high_score}', False, align=ALIGNMENT, font=FONTS)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open('data.txt', mode='w') as high_score:
            high_score.write(f'{self.high_score}')
        self.score = 0
        self.update_score()



    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER', False, align=ALIGNMENT, font=FONTS)





