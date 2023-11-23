import turtle
import os

class pattern():
    def __init__(self, angle: int, times: int):
        self.__angle = angle # Integer
        self.__times = times # Integer

    def draw_pattern(self):
        colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
        turtle.setup(800, 600)  # setting window dimensions
        turtle.bgcolor('black')
        for x in range(self.__times):
            turtle.pencolor(colors[x % 6])
            turtle.width(x / 100 + 1)
            turtle.forward(x)
            turtle.left(self.__angle)
        turtle.done()
      
    def open_file(self):
        try:
          i = 1
          with open("patterns.txt","r") as t:
            for lines in t:
              if i%2 != 0:
                self.__angle = int(lines)
              if i%2 == 0:
                self.__times = int(lines)
              i += 1
              if i%2 == 0:
                mypattern = pattern(self.__angle, self.__times)
                mypattern.draw_pattern()
        except OSError:
          print("cant find file, directory is", os.getcwd())



mypattern = pattern(120, 100)  # Demo pattern
mypattern.open_file()
