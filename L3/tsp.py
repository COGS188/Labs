import pygame
import random
import math
import sys
from tqdm import tqdm

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSP as CSP")

# Number of cities
num_cities = 10

cities = [(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)) for _ in range(num_cities)]

def draw_cities():
    screen.fill(BLACK)
    for city in cities:
        pygame.draw.circle(screen, WHITE, city, 5)
    pygame.display.update()

def draw_path(path, color):
    if path:
        pygame.draw.lines(screen, color, False, [cities[p] for p in path], 2)
        pygame.display.update()

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def csp_tsp():
    n = len(cities)
    path = []
    visited = [False] * n

    def path_cost(path):
        total_cost = 0
        for i in range(1, len(path)):
            # TODO: Add the distance between the current city and the previous city to total_cost
            
        # TODO: Add the distance from the last city back to the first to complete the circuit

        return total_cost

    def backtrack(current_path, progress):
        if len(current_path) == n:
            # TODO: Append the first city to current_path to complete the circuit

            nonlocal path
            if not path or path_cost(current_path) < path_cost(path):
                path = current_path[:]

            # TODO: Remove the last city from current_path after checking the path

            return # Nothing needs to be done after the path is complete
        
        # Recursive backtracking
        for next_city in range(n):
            if not visited[next_city]:
                visited[next_city] = True
                # TODO: Append the next city to current_path

                progress.update(1)
                backtrack(current_path, progress)
                # if backtracking is done, mark the city as unvisited and remove it from the path
                visited[next_city] = False
                current_path.pop()

    with tqdm(total=n*num_cities) as progress:
        for start_city in range(n):
            visited[start_city] = True
            backtrack([start_city], progress)
            visited[start_city] = False

    return path, path_cost(path)

def main():
    running = True
    path_found = False
    while running:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                running = False

        if not path_found:
            draw_cities()
            path, cost = csp_tsp()
            
            if path:
                draw_path(path, GREEN)
                print(f"Path found. Cost: {cost}")
                path_found = True

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
