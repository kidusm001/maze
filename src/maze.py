import time
import random
from geometry import Cell, Point

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        if seed is not None:
            random.seed(seed)
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        for i in range(self._num_cols):
            row_lst = []
            for j in range(self._num_rows):
                cell = Cell(self._win)
                row_lst.append(cell)
            self._cells.append(row_lst)
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell( self._num_cols -1, self._num_rows -1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))
            if i < len(self._cells)-1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))
            if j < len(self._cells[0])-1 and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            dir_idx = random.randrange(0, len(to_visit))
            chosen_i, chosen_j = to_visit[dir_idx]
            if chosen_i < i:
                self._cells[i][j].has_top_wall = False
                self._cells[chosen_i][chosen_j].has_bottom_wall = False
            elif chosen_i > i:
                self._cells[i][j].has_bottom_wall = False
                self._cells[chosen_i][chosen_j].has_top_wall = False
            elif chosen_j < j:
                self._cells[i][j].has_left_wall = False
                self._cells[chosen_i][chosen_j].has_right_wall = False
            elif chosen_j > j:
                self._cells[i][j].has_right_wall = False
                self._cells[chosen_i][chosen_j].has_left_wall = False
            self._break_walls_r(chosen_i, chosen_j)

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False
            
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return

        x1 = self._x1 + (j * self._cell_size_x)
        y1 = self._y1 + (i * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.02)
    
    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        if (
            i > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        if (
            i < self._num_cols - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        if (
            j > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        if (
            j < self._num_rows - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False
