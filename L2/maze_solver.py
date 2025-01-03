import pygame
import numpy as np
import heapq
import random
import math
import argparse

# Add a required argument that must be either "simulated_annealing" or "astar"
parser = argparse.ArgumentParser()
parser.add_argument("algorithm", help="Algorithm to solve the maze", choices=["simulated_annealing", "astar"])
args = parser.parse_args()

# Check the value of the argument
if args.algorithm == "simulated_annealing":
    print("Using Simulated Annealing")
elif args.algorithm == "astar":
    print("Using A*")
else:
    print(f"Invalid algorithm. Please run the script using 'python maze_solver.py <algorithm>' where <algorithm> is either 'simulated_annealing' or 'astar'")

# Constants
SCREEN_SIZE = 600
GRID_SIZE = 25
BLOCK_SIZE = SCREEN_SIZE // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Maze Solver")

# Maze representation (0 = open, 1 = wall)
maze = np.random.choice([0, 1], size=(GRID_SIZE, GRID_SIZE), p=[0.8, 0.2])
maze[0][0] = 0  # Start
maze[GRID_SIZE-1][GRID_SIZE-1] = 0  # Goal

# Function to draw the maze
def draw_maze(maze):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rect = pygame.Rect(x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, WHITE if maze[y][x] == 0 else BLACK, rect)
    start_rect = pygame.Rect(0, 0, BLOCK_SIZE, BLOCK_SIZE)
    goal_rect = pygame.Rect((GRID_SIZE-1)*BLOCK_SIZE, (GRID_SIZE-1)*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(screen, GREEN, start_rect)
    pygame.draw.rect(screen, RED, goal_rect)

# Function to draw the solution path
def draw_path(path):
    for position in path:
        rect = pygame.Rect(position[1]*BLOCK_SIZE, position[0]*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, BLUE, rect)

    start_rect = pygame.Rect(0, 0, BLOCK_SIZE, BLOCK_SIZE)
    goal_rect = pygame.Rect((GRID_SIZE-1)*BLOCK_SIZE, (GRID_SIZE-1)*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(screen, GREEN, start_rect)
    pygame.draw.rect(screen, RED, goal_rect)

# Heuristic function for A* (Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm Implementation
def astar(maze, start, goal):
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    close_set = set() # This is the set of nodes already evaluated
    came_from = {} # This is the map of navigated nodes, e.g. a dictionary where the key is the node and the value is the previous node in the path
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    oheap = []

    heapq.heappush(oheap, (fscore[start], start))
    
    while oheap:
        current = heapq.heappop(oheap)[1]

        if current == goal:
            path = []
            # TODO: Trace back the path from goal to start using came_from
            # and add each node to path list, then return reversed path

            return ...

        close_set.add(current)

        for i, j in neighbors:
            neighbor = (current[0] + i, current[1] + j)
            # TODO: Check if neighbor is within bounds and not a wall; continue to next neighbor if out of bounds or a wall
            
            # TODO: Calculate the potential g_score for the neighbor

            # TODO: If the potential g_score for neighbor is lower than gscore[neighbor], or the neighbor is not in the open heap:
            # - Update came_from to point to current
            # - Update gscore and fscore for neighbor
            # - Push neighbor onto the heap with updated fscore
            
    return False  # If no path is found

def get_neighbors(node):
        # Potential moves: up, down, left, right
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for move in moves:
            neighbor = (node[0] + move[0], node[1] + move[1])
            if 0 <= neighbor[0] < GRID_SIZE and 0 <= neighbor[1] < GRID_SIZE:
                if maze[neighbor[0]][neighbor[1]] == 0:  # Check if path is open
                    neighbors.append(neighbor)
        return neighbors

def get_random_neighbor(path):
    last_node = path[-1]
    neighbors = get_neighbors(last_node)
    if neighbors:
        return random.choice(neighbors)
    return last_node  # No available neighbors, return the current node

def simulated_annealing(maze, start, goal, temperature=1.0, cooling_rate=0.99, min_temperature=0.01):
    current_solution = [start]
    current_cost = heuristic(start, goal)

    while temperature > min_temperature:
        pass
        # TODO: Choose a random neighbor of the last node in current_solution

        # TODO: Extend the current_solution with this new node

        # TODO: Calculate the cost for moving to this new node using heuristic

        # TODO: Calculate cost difference between new cost and current cost

        # TODO: Decide whether to accept the new solution based on the acceptance probability
        # Hint: Accept if the new cost is better, or based on the probability exp(-cost_diff / temperature)

        # TODO: If the last node in current_solution is the goal, return the solution

        # TODO: Apply cooling rate to temperature

    return None  # Return None if no solution found after cooling to minimum temperature


def solve_maze(maze):
    start = (0, 0)
    goal = (GRID_SIZE - 1, GRID_SIZE - 1)
    if args.algorithm == "simulated_annealing":
        path = simulated_annealing(maze, start, goal)
    elif args.algorithm == "astar":
        path = astar(maze, start, goal)
    if not path:
       return None
    return path[::-1]  # Reverse path

# Main loop
running = True
maze_solved = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    draw_maze(maze)

    # Solve the maze and draw the solution path
    if not maze_solved:
        path = solve_maze(maze)
        if path:
            maze_solved = True

    if maze_solved:
        draw_path(path)

    new_map_rect = pygame.Rect(SCREEN_SIZE - 150, 0, 150, 50)
    pygame.draw.rect(screen, RED, new_map_rect)
    font = pygame.font.Font(None, 36)
    text = font.render("New Map", True, WHITE)
    text_rect = text.get_rect(center=new_map_rect.center)
    screen.blit(text, text_rect)

    # If algorithm is simulated_annealing, also add a button called "Try Again" that will re-run the algorithm
    if args.algorithm == "simulated_annealing":
        try_again_rect = pygame.Rect(SCREEN_SIZE - 150, 60, 150, 50)
        pygame.draw.rect(screen, BLUE, try_again_rect)
        text = font.render("Try Again", True, WHITE)
        text_rect = text.get_rect(center=try_again_rect.center)
        screen.blit(text, text_rect)

    # Check if the user clicked the try_again button
    if event.type == pygame.MOUSEBUTTONDOWN and args.algorithm == "simulated_annealing":
        if try_again_rect.collidepoint(event.pos):
            maze_solved = False

    # Check if the user clicked the new_map button
    if event.type == pygame.MOUSEBUTTONDOWN:
        if new_map_rect.collidepoint(event.pos):
            maze_solved = False
            maze = np.random.choice([0, 1], size=(GRID_SIZE, GRID_SIZE), p=[0.8, 0.2])
            maze[0][0] = 0  # Start
            maze[GRID_SIZE-1][GRID_SIZE-1] = 0  # Goal

    pygame.display.flip()

pygame.quit()

