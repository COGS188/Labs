# Lab 3: AC-3 Planning, Adversarial Games, and Constrained-Oriented Games (5 points)

**Deadline**: Wednesday, May 1, 2024 at 11:59pm on Gradescope

This assignment has 3 parts.

## Installations

I strongly recommend you work on this assignment on your local machine, rather than on DataHub. This is because we use Pygame, which requires a graphical interface to run. The terminal on DataHub does not let you directly open a window for Pygame and it may not work on Jupyter notebooks either. If there are any technical issues with running the code on your local machine, please reach out to us on EdStem as soon as possible and we can help you troubleshoot.

Before running the script, ensure you have the following modules installed on your system:

* Pygame
* Numpy
* Shapely
* Scipy
* Tqdm
* Argparse

You can install these modules using pip:

```bash
pip install pygame numpy shapely scipy tqdm argparse
```

## Part 1: AC-3 Planning for Map Coloring (1.5 points)

This part will help you understand the concepts of constraint satisfaction problems (CSP) using a practical example: coloring a map such that no two adjacent regions have the same color. You'll employ two key algorithms that you studied in the lectures: the Arc Consistency Algorithm #3 (AC-3) and backtracking.

### Running the Game

The main Python script that you'll run is `map_coloring.py`. It contains all the logic for generating the map, applying the AC-3 algorithm, using backtracking for coloring, and drawing the game interface. 

To run the game, navigate to the project directory in your terminal or command prompt and execute:
    
```bash
python map_coloring.py
```

**Note**: running the code won't work unless you fix the code in `map_coloring.py` as described below.

### Conceptual Overview

**Voronoi Diagram**

The map is divided into regions using a Voronoi diagram, which partitions the space into regions based on distance to a set of points. Each region represents an area that needs to be colored without sharing the same color with its adjacent regions. We have already implemented the Voronoi diagram generation for you, and this just allows us to partition a polygon-shaped map into regions.

**Constraint Satisfaction Problem (CSP)**

This lab models the map coloring as a CSP, where each region's color is a variable, and the constraint is that no two adjacent regions can share the same color.

### Parts of the Code

#### Voronoi Diagram Generation:
* Function `generate_voronoi_regions(num_regions)`: Generates random points and creates Voronoi regions bounded within the game screen. Each region is initialized with a neutral gray color, which means it has not been colored yet.
#### Neighbor Determination:
* Function `determine_neighbors(vor, regions)`: Determines which regions are adjacent to each other based on the shared edges in the Voronoi diagram.
#### Drawing the Map:
* Function `draw_map()`: Responsible for drawing the regions and their borders on the screen, along with the current coloring.
#### AC-3 Algorithm:
* Function `apply_ac3()`: Implements the AC-3 algorithm to reduce the possible colors for each region by ensuring arc consistency.
* Function `remove_inconsistent_values(xi, xj)`: Checks and possibly reduces the color domain of region xi based on the domain of xj.
#### Backtracking:
* Function `backtrack(region_index)`: Recursively tries to color the map, backtracking when it encounters a region that cannot be colored without violating constraints.
* Function `is_valid(region, color)`: Checks if the current color choice for a region is valid (i.e., does not conflict with the colors of neighboring regions).

### Assignment Instructions

Here are the tasks to be completed:

1. Implement the `remove_inconsistent_values` function:
    You need to iterate over each color in the domain of xi and check if it conflicts with all colors in xj's domain. Remove conflicting colors and return whether any changes were made.

2. Complete the `apply_ac3` function:
    Implement the logic to initialize and process the queue of region pairs, using the `remove_inconsistent_values` function to enforce consistency.

3. Finish the `backtrack` function:
    Implement the recursion logic to attempt coloring each region, verifying the validity of each color choice, and handling backtracking correctly.

The above functions have "TODO" comments that indicate where you need to write your code. You can also add additional helper functions if needed. However, please do not modify the existing function signatures and return types.

### Testing

To run the game, execute the following command:

```bash
python map_coloring.py
```

When you run the game, you will see a map with regions that need to be colored. If no color is assigned to a particular region, it will be displayed in gray. Once you complete the AC-3 algorithm and backtracking, the regions will be colored based on the constraints.

To check that your code is working correctly, you can try different numbers of regions and observe the coloring results. You can also modify the `NUM_REGIONS` variable in the script to test with different numbers of regions. You should see that the regions are colored correctly without any adjacent regions sharing the same color.

Also, if you re-run the game, you should see different maps generated each time. This is because the Voronoi diagram used to generate the regions is randomized.

## Part 2: Adversarial Games: Minimax and Alpha-Beta Pruning on a Connect-4 Game (2.5 points)

In this part, you will develop and enhance a Connect Four game using Python and Pygame. The game can be played in two modes: human vs. human and human vs. AI. Your main task is to implement parts of the AI using the Minimax algorithm with alpha-beta pruning to make the AI competitive.

To get a feeling of how the connect-4 game works, run the following command:

```bash
python connect_four.py human
```

This sets the game mode to human vs. human. You can play the game by clicking on the columns to drop your pieces. The game will alternate between the two players until one player wins or the board is full (resulting in a draw).

### Code Organization

* **Main Modules:**
  * `create_board()`: Initializes and returns a 6x7 grid representing the game board.
  * `drop_piece(board, row, col, piece)`: Drops a piece into the board.
  * `is_valid_location(board, col)`: Checks if a column can receive another piece.
  * `get_next_open_row(board, col)`: Finds the next open row in the specified column.
  * `winning_move(board, piece)`: Checks if the last move was a winning move.
  * `draw_board(board)`: Graphically represents the board state using Pygame.
* **AI Logic:**
  * `minimax(board, depth, alpha, beta, maximizingPlayer)`: Contains the logic for the Minimax algorithm with alpha-beta pruning. **This is where you will focus your implementation efforts.**
  
* **Utility Functions:**
  * `is_terminal_node(board)`: Determines if the board is in a terminal state (game over or full board).
  * `get_valid_locations(board)`: Returns a list of columns that can accept more pieces.

### Assignment Tasks

You are required to complete the following tasks in the `minimax` function:

1. __Base Case Logic:__ Implement the base case for the recursion. Determine what should happen when the game reaches a terminal state or the specified depth is zero.
2. __Heuristic Evaluation:__ When the depth is zero and the game isn't over, you should evaluate the board using a heuristic function. Implement or improve the score_position(board, piece) function to calculate the heuristic value of the board.
3. __Recursive Minimax Logic:__ Implement the recursive calling of the minimax function to explore possible future game states.
4. __Alpha-Beta Pruning:__ Add logic to prune branches of the game tree that don't need to be explored, which will enhance the performance of the AI.

The `minimax` function has "TODO" comments that indicate where you need to write your code. You can also add additional helper functions if needed. However, please do not modify the existing function signatures and return types.

### Expected Outcomes

After completing the Minimax algorithm, the AI should be able to play against a human competitively. The AI should be pretty good at finding winning moves and blocking the opponent from winning. The AI should also be able to recognize when the game is a draw and act accordingly. **Overall, your AI should be pretty hard to beat!**

### Testing

To run the Connect Four game with the AI, execute the following command:

```bash
python connect_four.py ai
```

When you run the script, you will see a window with the Connect Four game board. You can play against the AI by clicking on the columns to drop your pieces. The AI will take its turn after you make your move. The game will continue until one player wins or the board is full.

You are encouraged to play against the AI to test its performance and see how well it plays. You can also modify the depth of the Minimax algorithm in the script to see how it affects the AI's performance. Keep in mind that increasing the depth will make the AI more competitive but will also increase the time it takes to make a move.

## Part 3: Constrained-Oriented Games: Solving the 8-Queens Problem (1 point)

In this final task, you will develop a solution to the classic 8 Queens puzzle using Python and Pygame. The challenge is to place eight queens on a standard chessboard so that no two queens threaten each other. This means that no two queens can share the same row, column, or diagonal.

### Code Organization

**Main Functions:**
* `draw_board()`: Draws an 8x8 chessboard on the window.
* `place_queens(queen_positions)`: Places images of queens on the board based on their positions.
* `is_safe(board, row, col)`: Determines if it is safe to place a queen at the given position.
* `solve_8_queens(board, col)`: Recursively attempts to place queens on the board using backtracking.
* `update_board()`: Initializes the board and finds a valid arrangement of queens.
* `main()`: Contains the main game loop which handles events and updates the display.

### Assignment Tasks

You need to complete several parts of the given code to make the application work:

1. `is_safe` Function: 
  * Implement the logic to check if placing a queen at (row, col) is safe. You should check for conflicts along the row, and both upper and lower diagonals.
2. `solve_8_queens` Function:
  * Complete the loop to iterate through each row in the current column.
  * Implement the condition to check if placing a queen is safe.
  * Fill in the backtrack step which removes a queen if placing it leads to no solution.

### Expected Outcomes

To test your implementation, run the following command:

```bash
python 8_queens.py
```

Upon successfully running the program, the chessboard will display with eight queens placed such that no queen is under threat from another. This will be visualized in real-time as the program computes the positions. If no solution is found, the board will remain empty. It's pretty easy to see if the solution is correct by observing the board and checking that no two queens are in the same row, column, or diagonal.

For further exploration, you can try modifying the code to solve the N-Queens problem for different board sizes. The 8-Queens problem is a classic example, but the solution can be generalized to any size board.


## Optional, Ungraded Problem: Solving the Traveling Salesman Problem as a CSP (0 points)

In this part, you will implement a solution to the Travelling Salesman Problem (TSP) using a constraint satisfaction approach. The TSP is a classic algorithmic problem in the field of computer science and operations research, focusing on optimization. The goal of the TSP is to traverse a number of cities, visiting each city exactly once, returning to the original city, with the shortest possible route.

### Problem Setup
* __Cities__: The cities are randomly generated points on a 2D plane within the window of the application.
* __Objective__: The objective is to find the shortest possible route that visits each city exactly once and returns to the starting point.

### Parts of the Code

* __Pygame Setup:__
    Initializes the Pygame window and sets up basic configurations.
* __City Generation:__
    `cities`: A list of tuples where each tuple represents the coordinates of a city on the display.
* __Drawing Functions:__
    `draw_cities()`: Draws each city on the screen as a white dot.
    `draw_path(path, color)`: Draws lines between cities to represent the path of the salesman.
* __Utility Function:__
    `euclidean_distance(city1, city2)`: Computes the Euclidean distance between two cities.
* __TSP Solver:__
    `csp_tsp()`: Contains the logic to solve the TSP using a constraint satisfaction model with backtracking.

### Details of the `csp_tsp()` Function

* __Variables:__
    `n`: The number of cities.
    `path`: List that will hold the best path found.
    `visited`: A list to keep track of visited cities.
* __Internal Functions:__
    `path_cost(path)`: Computes the total travel distance of the salesman for a given path.
    `backtrack(current_path, progress)`: The main recursive function used to explore all possible routes and update the path if a better one is found.

### Assignment Instructions

Your task is to complete the following parts of the `csp_tsp()` function:

1. __Path Cost Calculation:__
    Inside the `path_cost` function, calculate the total travel distance of the path. This includes the sum of the distances between consecutive cities in the path and the distance to return to the starting city.
2. __Complete the Circuit:__
    In the `backtrack` function, ensure that the path is completed by returning to the starting city once all cities have been visited.
3. __City Addition and Removal in Path:__
    Manage the list of visited cities and the current path as you explore different configurations with backtracking.

The above functions have "TODO" comments that indicate where you need to write your code. You can also add additional helper functions if needed. However, please do not modify the existing function signatures and return types.

### Testing

To run the TSP solver, execute the following command:

```bash
python tsp.py
```

When you run the script, you will see a window with randomly generated cities shown as white dots on a black background. After you implement the solver, it will attempt to find the shortest path that visits each city exactly once and returns to the starting city. The path will be displayed in green. The expected result should be a path that connects all cities in the shortest possible distance.

You can modify the number of cities by changing the `num_cities` variable in the script. Keep in mind that the time to find the optimal path increases exponentially with the number of cities. If you re-run the script, you should see different city configurations each time, as the cities are randomly generated.

If you take COGS 186 (Genetic Algorithms) sometime in the future, you will learn how to solve the TSP using genetic algorithms, which is another interesting approach to this problem that can provide reasonably close solutions for much larger numbers of cities with less computation time than the constraint satisfaction approach.

## Submission

Submit the following files to Gradescope:

1. `map_coloring.py`
2. `connect_four.py`
3. `8_queens.py`

(Submitting the optional problem is not required.)

Make sure to save your files before submitting them. You can submit as many times as you like before the deadline. Only the last submission will be graded.

We hope you find this lab fun and engaging!