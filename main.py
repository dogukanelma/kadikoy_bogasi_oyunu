import turtle
import time
from random import random
import winsound


class KadikoyBogasi:
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.setup(width=800, height=800, startx=0, starty=0)
        self.wn.title("Kadıköy Boğası")
        self.wn.bgcolor("white")

        turtle.register_shape("boga.gif")
        self.t = turtle.Turtle()
        self.t.shape("boga.gif")
        self.t.color("black")
        self.t.penup()
        self.t.home()

        self.screen_right = self.wn.window_width() / 3 - 50
        self.screen_left = -self.wn.window_width() / 3 + 50
        self.screen_top = self.wn.window_height() / 3 - 50
        self.screen_bottom = -self.wn.window_height() / 3 + 50

        self.xvel = 1
        self.yvel = 1

        self.text_turtle = turtle.Turtle()
        self.text_turtle.hideturtle()
        self.text_turtle.penup()
        top_height = self.wn.window_height() / 2
        text_y = top_height - top_height / 5
        self.text_turtle.setposition(0, text_y)

        self.score_turtle = turtle.Turtle()
        self.score_turtle.hideturtle()
        self.score_turtle.penup()
        self.score_turtle.setposition(225,-375)

        self.countdown = 15
        self.score = 0
        self.is_moving = False

        self.wn.onclick(self.on_click)

    def on_click(self, x, y):
        if self.is_moving and self.t.distance(x, y) < 20 and self.t.isvisible():
            self.score += 1
            self.score_turtle.clear()
            self.score_turtle.write("Score: %s" % self.score, align="center", font=("None", 40))
            winsound.PlaySound('boga_sound.wav', winsound.SND_FILENAME)

    def timer_begin(self):
            self.text_turtle.clear()
            self.text_turtle.write("Oyun Başladı", align="center", font=("None", 40))
            self.is_moving = True
            self.wn.ontimer(self.Timer, 1000)
            self.boga_yurur()

    def Timer(self):
        self.text_turtle.clear()
        self.text_turtle.write("Timer: %s" % self.countdown, align="center", font=("None", 40))
        self.score_turtle.clear()
        self.score_turtle.write("Score: %s" % self.score, align="center", font=("None", 40))
        self.countdown -= 1
        if self.countdown >= 0:
            self.wn.ontimer(self.Timer, 1000)

        else:
            self.is_moving = False
            self.timer_end()

    def timer_end(self):
        self.text_turtle.clear()
        self.text_turtle.write("Oyun Bitti", align="center", font=("None", 40))
        self.t.hideturtle()

    def boga_yurur(self):
        if self.is_moving:
            self.boga_hide()
            steps = int(random() * 350)
            angle = int(random() * 360)
            self.t.right(angle)
            self.t.forward(steps * self.xvel * self.yvel)

            x, y = self.t.position()


            if x > self.screen_right:
                self.xvel *= -1
                self.t.setx(self.screen_right)
            elif x < self.screen_left:
                self.xvel *= -1
                self.t.setx(self.screen_left)

            if y > self.screen_top:
                self.yvel *= -1
                self.t.sety(self.screen_top)
            elif y < self.screen_bottom:
                self.yvel *= -1
                self.t.sety(self.screen_bottom)

            self.wn.ontimer(self.boga_yurur, 400)
            self.boga_show()


    def start(self):
        self.t.showturtle()
        self.timer_begin()
        self.wn.mainloop()


    def boga_hide(self):
        self.t.hideturtle()

    def boga_show(self):
        self.t.showturtle()

game = KadikoyBogasi()
game.start()



