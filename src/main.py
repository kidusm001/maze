from window import Window
from geometry import Line, Point, Cell

def main():
    win = Window(800,800)
    p1 = Point(1, 1)
    p2 = Point(20, 20)
    cell = Cell(win)
    cell.draw(p1.x, p1.y, p2.x, p2.y)
    p3 = Point(100, 100)
    p4 = Point(20, 20)
    cell1 = Cell(win)
    cell1.draw(p4.x, p4.y, p3.x, p3.y)
    cell.draw_move(cell1)
    cell2 = Cell(win)
    cell2.draw(20,1,40,20)
    cell.draw_move(cell2, True)

    win.wait_for_close()

if __name__ == "__main__":
    main()