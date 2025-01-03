# Lab 2: Solving a Maze Using A* Search and Simulated Annealing (5 points)

**Deadline**: Monday, April 22, 2024 at 11:59pm on Gradescope

This lab assignment implements a maze-solving application using Pygame for visualization. The application supports two algorithms for solving the maze: A* and Simulated Annealing. You are required to complete parts of both algorithms to make the maze solver functional.

## File Description

All the code for this assignment will be done in `maze_solver.py`. This is the main Python script that you will run. It sets up the maze, visualizes it, and solves it using one of the two algorithms specified by a command-line argument.

## Installations

I strongly recommend you work on this assignment on your local machine, rather than on DataHub. This is because we use Pygame, which requires a graphical interface to run. The terminal on DataHub does not let you directly open a window for Pygame and it may not work on Jupyter notebooks either. If there are any technical issues with running the code on your local machine, please reach out to us on EdStem as soon as possible and we can help you troubleshoot.

Before running the script, ensure you have Python and Pygame installed on your system. You can install Pygame using pip:

```bash
pip install pygame
pip install numpy
```

## Usage

Run the script from the command line by specifying the algorithm you want to use:

```bash
python maze_solver.py astar
```

or

```bash
python maze_solver.py simulated_annealing
```

## Functions to Complete

You are expected to complete the following functions:

* `astar(maze, start, goal)`: Implement the A* pathfinding algorithm.
* `simulated_annealing(maze, start, goal, temperature, cooling_rate, min_temperature)`: Implement the Simulated Annealing algorithm for solving the maze.

## Provided Functions and Variables

* `draw_maze(maze)`: Draws the maze grid where white blocks represent open paths and black blocks represent walls.
* `draw_path(path)`: Highlights the path found by the algorithms in blue.
* `heuristic(a, b)`: Calculates the Manhattan distance between two points, used by the A* algorithm.
* `get_neighbors(node)`: Returns valid moves from the current node.
* `get_random_neighbor(path)`: Returns a random valid move from the last node in the current path, used in Simulated Annealing.

## GUI Elements

* **New Map Button**: This button generates a new random maze. Useful for testing the algorithms multiple times on different randomized mazes.
* **Try Again Button (Simulated Annealing only)**: Since simulated annealing can produce different results due to its probabilistic nature, this button allows re-running the algorithm on the same maze.

## Assignment Tasks

1. Complete the `astar` function: Implement the core logic of the A* algorithm.
2. Complete the `simulated_annealing` function: Implement the core logic of the Simulated Annealing algorithm.
3. Test both algorithms: Use different mazes to ensure that your implementations correctly solve the maze.

Each of the functions above has a set of "TODO" comments that indicate where you need to write your code. You can also add additional helper functions if needed. However, please do not modify the existing function signatures and return types. You are welcome to experiment with different starting points, goals, and maze configurations to test your implementations.

## Submission

Submit the `maze_solver.py` file to Gradescope with your completed functions. Make sure to save your file before submitting!
