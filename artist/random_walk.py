import os
import random
import time


class Walker:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def random_move(self):
        self.move(random.choice([1, 2, 3, 4, 5, 6, 7, 8]))

    def move(self, dir):
        if dir == 1:
            self.go_left()
        elif dir == 2:
            self.go_right()
        elif dir == 3:
            self.go_down()
        elif dir == 4:
            self.go_up()
        elif dir == 5:
            self.go_left()
            self.go_up()
        elif dir == 6:
            self.go_left()
            self.go_down()
        elif dir == 7:
            self.go_right()
            self.go_up()
        elif dir == 8:
            self.go_right()
            self.go_down()

    def go_left(self):
        self.pos_x -= 1
    def go_right(self):
        self.pos_x += 1
    def go_down(self):
        self.pos_y += 1
    def go_up(self):
        self.pos_y -= 1


class Window:
    shape_dot = "#"
    def __init__(self):
        term_size = os.get_terminal_size()
        self.win_col, self.win_row = term_size.columns, term_size.lines

    def clear(self):
        print("\n" * self.win_row)

    def draw(self, dots: [Walker]):
        # TODO chage this method to displya multiple dots...
        # line_counter = 0
        print( "\n" * (dots[0].pos_y) , end=None)
        print(f"{' ' * (dots[0].pos_x - 1)}{self.shape_dot}", end=None)
        print( "\n" * (self.win_row - dots[0].pos_y) )
        """
        for dot in sorted(dots, key=lambda x: x.pos_y):
            # what if dot exists at same line...?
            print( "\n" * (dot.pos_y - 1) )
        """


class Direction:
    left = 1
    right = 2
    down = 3
    up = 4

    @staticmethod
    def get_random_dir(self):
        return random.choise([1, 2, 3, 4])


if __name__ == "__main__":
    win = Window()
    center_x, center_y = win.win_col // 2, win.win_row // 2
    dot = Walker(center_x, center_y)
    for i in range(1000):
        win.draw([dot])
        dot.random_move()
        time.sleep(0.1)
    
