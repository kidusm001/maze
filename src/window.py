from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze")
        self.canvas = Canvas(self.root, bg="white",height=height,width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.window_run = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.window_run = True
        while self.window_run:
            self.redraw()
    
    def close(self):
        self.window_run = False