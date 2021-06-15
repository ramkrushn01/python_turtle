from turtle import *
from random import choice
import numpy as np


class Drawpic(Turtle):

    def runMe(self, x, y, diff):
        self.up()
        self.goto(x, y)
        self.down()
        self.forward(diff)

    def drawMe(self, xvarList, yvarList, difXList, Pencolor):
        self.speed(10)
        self.pencolor(Pencolor)
        self.up()
        self.goto(-600, 400)
        self.down()
        for i in range(len(xvarList)-1):
            self.pencolor(Pencolor)
            x = (xvarList[i])-600
            y = -(yvarList[i])+400
            diff = difXList[i]
            self.runMe(x, y, diff)


if __name__ == "__main__":
    bgcolors = ['red', 'orange', 'green',
                'white', 'blue']  # for backgound color
    inputImg = np.fromfile('shivVal',dtype=int)  # get a Input Image Path
    
    window = Screen()
    # To Change The Backgrond color On Click On Window
    window.onclick(lambda x, y: window.bgcolor(choice(bgcolors)))

    window.colormode(255)
    a = inputImg[:5655]
    b = inputImg[5655:11309]
    c = inputImg[11310:]

    pin = Drawpic()
    pin.drawMe(a,b ,c, 'black')


    window.mainloop()
