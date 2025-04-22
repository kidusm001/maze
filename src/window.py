from tkinter import Tk, BOTH, Canvas
from geometry import Line

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze")
        self.__canvas = Canvas(self.__root, bg="white",height=height,width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__window_run = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__window_run = True
        while self.__window_run:
            self.redraw()
    
    def close(self):
        self.__window_run = False

    def draw_line(self, line: Line, fill_color="black", width=3):
        line.draw(self.__canvas, fill_color, width)

    def draw_circle(self, x, y, r, fill_color="red"):
        self.__canvas.create_oval(x - r, y - r, x + r, y + r, fill=fill_color, outline=fill_color)
