
import random # For the dice
import os # For the centered print


class Dice:
    def __init__(self,sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1,self.sides)

    def roll_and_add(self,add=0):
        return random.randint(1,self.sides) + add




class Text:
    def __init__(self):
        pass

    def centered_print(text):
        width = os.get_terminal_size().columns
        print(text.center(width))

    def line_spacer_print(char="="):
        if char == "":
            char = "="
        for i in range(os.get_terminal_size().columns):
            print(char, end='')

    def left_print(text):
        print('{:>75}'.format(text))

    def right_print(text):
        print('{:>155}'.format(text))

    def centered_title_print(text,char="="):
        if char == "":
            char = "="
        width = (os.get_terminal_size().columns / 2) - (len(text) + 1)
        for i in range(int(width)):
            print(char, end='')
        print("{ " + text.upper() + " }", end='')
        for i in range(int(width)):
            print(char, end='')
        print("")

    def left_right_print(left,right):
        width = int(os.get_terminal_size().columns / 2)
        for i in range(int(width/2)):
            print(" ", end='')
        print('{}{}{}'.format(left, ' '*(width-len(left+right)), right))
        print("")





