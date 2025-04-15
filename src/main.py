from window import Window
from geometry import Line, Point

def main():
    win = Window(800,800)
    p1 = Point(1, 1)
    p2 = Point(20, 22)
    line = Line(p1, p2)
    win.draw_line(line, "black")
    win.wait_for_close()

if __name__ == "__main__":
    main()