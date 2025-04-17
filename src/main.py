from window import Window
from geometry import Line, Point, Cell
from maze import Maze

def main():
    win = Window(800,800)
    maze = Maze(0, 0, 10,10, 20, 20, win)
    maze._create_cells()

    win.wait_for_close()

if __name__ == "__main__":
    main()