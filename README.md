# Maze

This project is a maze generator and solver built using Python. It uses the Tkinter library for graphical rendering and provides a visual representation of the maze and its solution.

## Features
- Generates a random maze with customizable dimensions and cell sizes.
- Solves the maze using a recursive backtracking algorithm.
- Visualizes the maze generation and solving process in real-time.

## Requirements
- Python 3.x
- Tkinter (usually included with Python installations)

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/kidusm001/maze
   cd maze
   ```
2. Run the project:
   ```bash
   ./build.sh
   ```
3. A window will open displaying the maze. The maze will be generated and solved automatically.

## Customization
You can modify the maze dimensions, cell sizes, and other parameters in the `main.py` file:
```python
num_rows = 20  # Number of rows in the maze
num_cols = 45  # Number of columns in the maze
cell_size_x = 20  # Width of each cell
cell_size_y = 20  # Height of each cell
```

## Dependencies
This project uses the Tkinter library for GUI rendering. Tkinter is included with most Python installations, but if it's not available, you can install it as follows:

### Installing Tkinter
- On Debian/Ubuntu-based systems:
  ```bash
  sudo apt-get install python3-tk
  ```
- On macOS (if not already included):
  ```bash
  brew install python-tk
  ```
- On Windows: Tkinter is included with the standard Python installer. Ensure you have Python installed from [python.org](https://www.python.org/).

## License
This project is licensed under the MIT License.
