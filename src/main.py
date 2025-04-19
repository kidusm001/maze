from window import Window
from geometry import Line, Point, Cell
from maze import Maze

def main():
    win = Window(800,800)
    maze = Maze(10, 10, 5,10, 20, 20, win, 0)
    

    win.wait_for_close()

if __name__ == "__main__":
    main()