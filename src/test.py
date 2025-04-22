import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    # def test_maze_cell_size(self):
    #     cell_size_x = 20
    #     cell_size_y = 30
    #     m = Maze(0, 0, 200, 200, cell_size_x, cell_size_y)
    #     self.assertEqual(m._cell_size_x, cell_size_x)
    #     self.assertEqual(m._cell_size_y, cell_size_y)
    
    def test_maze_initialization_position(self):
        x = 100
        y = 150
        m = Maze(x, y, 5, 5, 10, 10)
        self.assertEqual(m._x1, x)
        self.assertEqual(m._y1, y)

    def test_maze_different_dimensions(self):
        num_cols = 5
        num_rows = 8
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m._cells), num_cols)
        self.assertEqual(len(m._cells[0]), num_rows)

    def test_maze_break_wall(self):
        m = Maze(5, 5, 5, 5, 20, 20)
        m._break_entrance_and_exit()
        self.assertEqual(m._cells[0][0].has_top_wall, False)
        self.assertEqual(m._cells[m._num_cols - 1][m._num_rows - 1].has_bottom_wall, False)
    
    def test_maze_reset_visited(self):
        m = Maze(5, 5, 5, 5, 20, 20)
        for i in range(len(m._cells)):
            for j in range(len(m._cells[i])):
                self.assertEqual(m._cells[i][j].visited, False)
if __name__ == "__main__":
    unittest.main()