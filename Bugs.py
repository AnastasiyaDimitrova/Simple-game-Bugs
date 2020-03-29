import math
import random
import bugs

win_l = 700
win_h = 700

bug = 5

bug.screensize(win_h, win_l)


class runner(object):
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.bug = bug.Бug()
        self.bug.shape('')
        self.bug.color(color)
        self.bug.penup()
        self.bug.setpos(pos)
        self.bug.setheading(100)

    def move(self):
        b = random.randrange(1, 22)
        self.pos = (self.pos[0], self.pos[1] + b)
        self.bug.pendown()
        self.bug.forward(b)