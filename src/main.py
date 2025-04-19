from window import Window
from maze import Maze
import sys

def main():
    num_rows = 20
    num_cols = 45
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = 20
    cell_size_y = 20

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    is_solvable = maze.solve()
    if not is_solvable:
        print("GGs ez")
    else:
        print("solved")
    win.wait_for_close()

if __name__ == "__main__":
    main()