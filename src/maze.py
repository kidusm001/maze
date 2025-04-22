import time
import random
from collections import deque
from geometry import Cell, Line, Point

class Maze():
    """
    Maze grid with generation and solving visualization.
    """
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
        self._cells = []
        for i in range(self._num_cols):
            row_lst = []
            for j in range(self._num_rows):
                cell = Cell(self._win)
                row_lst.append(cell)
            self._cells.append(row_lst)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

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

    def _animate(self, sleep_time=0.005):
        self._win.redraw()
        time.sleep(sleep_time)

    def _solve_bfs_core(self):
        start = (0, 0)
        goal = (self._num_cols - 1, self._num_rows - 1)
        queue = deque()
        queue.append(start)
        prev = {}
        visited = [[False for _ in range(self._num_rows)] for _ in range(self._num_cols)]
        visited[start[0]][start[1]] = True
        found = False
        while queue:
            i, j = queue.popleft()
            if (i, j) == goal:
                found = True
                break
            neighbors = [
                (-1, 0, 'has_top_wall', 'has_bottom_wall'),
                (1, 0, 'has_bottom_wall', 'has_top_wall'),
                (0, -1, 'has_left_wall', 'has_right_wall'),
                (0, 1, 'has_right_wall', 'has_left_wall')
            ]
            for di, dj, wall_c, wall_n in neighbors:
                ni, nj = i + di, j + dj
                if 0 <= ni < self._num_cols and 0 <= nj < self._num_rows and not visited[ni][nj]:
                    if not getattr(self._cells[i][j], wall_c) and not getattr(self._cells[ni][nj], wall_n):
                        visited[ni][nj] = True
                        prev[(ni, nj)] = (i, j)
                        queue.append((ni, nj))
        if not found:
             return None
        path = []
        cur = goal
        if cur != start and cur not in prev:
             return None
        while cur != start:
            path.append(cur)
            cur = prev[cur]
        path.append(start)
        path.reverse()
        return path

    def solve(self):
        self._reset_cells_visited()
        self._solve_dfs_animate(0, 0)

    def _solve_dfs_animate(self, i, j):
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        neighbors = [
            (-1, 0, 'has_top_wall', 'has_bottom_wall'),
            (1, 0, 'has_bottom_wall', 'has_top_wall'),
            (0, -1, 'has_left_wall', 'has_right_wall'),
            (0, 1, 'has_right_wall', 'has_left_wall')
        ]
        for di, dj, wall_c, wall_n in neighbors:
            ni, nj = i + di, j + dj
            if 0 <= ni < self._num_cols and 0 <= nj < self._num_rows:
                if not self._cells[ni][nj].visited and not getattr(self._cells[i][j], wall_c) and not getattr(self._cells[ni][nj], wall_n):
                    self._draw_snake_segment(i, j, ni, nj)
                    self._animate(0.01)
                    if self._solve_dfs_animate(ni, nj):
                        return True
                    self._draw_snake_segment(i, j, ni, nj, head=False, color="lightgrey")
                    self._animate(0.01)
        return False

    def _draw_snake_segment(self, i1, j1, i2, j2, head=False, color="red"):
        c1 = self._cells[i1][j1]
        c2 = self._cells[i2][j2]
        x1 = (c1._x1 + c1._x2) / 2
        y1 = (c1._y1 + c1._y2) / 2
        x2 = (c2._x1 + c2._x2) / 2
        y2 = (c2._y1 + c2._y2) / 2
        snake_line = Line(Point(x1, y1), Point(x2, y2))
        self._win.draw_line(snake_line, fill_color=color, width=6)
        if head and color == "red":
            r = min((c2._x2 - c2._x1), (c2._y2 - c2._y1)) * 0.35
            self._win.draw_circle(x2, y2, r, fill_color="red")