import pygame
import sys
import numpy as np
from scipy.spatial import Voronoi
from shapely.geometry import Polygon, box

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
BACKGROUND_COLOR = (255, 255, 255)  # White
LINE_COLOR = (0, 0, 0)  # Black
NUM_REGIONS = 20  # Desired number of regions

colors = {
    'R': (255, 0, 0),    # Red
    'B': (0, 0, 255),    # Blue
    'Y': (255, 255, 0),  # Yellow
    'G': (0, 255, 0)     # Green
}

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Map Coloring Game")
clock = pygame.time.Clock()

buffer = 30
boundary = box(buffer, buffer, WIDTH - buffer, HEIGHT - buffer)

# Generate random points and create Voronoi regions
def generate_voronoi_regions(num_regions):
    regions = {}
    attempts = 0
    while len(regions) < num_regions and attempts < 100:
        attempts += 1
        points = np.random.rand(num_regions * 2, 2) * np.array([WIDTH, HEIGHT])
        vor = Voronoi(points)
        temp_regions = {}
        for idx, region in enumerate(vor.point_region):
            vertices = vor.regions[region]
            if all(v >= 0 for v in vertices):  # Check if region is bounded
                polygon = Polygon([vor.vertices[v] for v in vertices])
                clipped_polygon = polygon.intersection(boundary)
                if not clipped_polygon.is_empty:
                    temp_regions[chr(65 + idx % 26)] = {
                        'points': list(clipped_polygon.exterior.coords),
                        'color': (128, 128, 128)  # Initialize with a neutral gray color
                    }

        # Select the first NUM_REGIONS valid regions
        if len(temp_regions) >= num_regions:
            regions = dict(list(temp_regions.items())[:num_regions])

    return regions, vor

regions, vor = generate_voronoi_regions(NUM_REGIONS)
color_domains = {key: list(colors.keys()) for key in regions}

# Determine neighbors from Voronoi diagram
def determine_neighbors(vor, regions):
    neighbors = {key: [] for key in regions.keys()}
    for ridge_points in vor.ridge_points:
        region1, region2 = chr(65 + ridge_points[0] % 26), chr(65 + ridge_points[1] % 26)
        if region1 in regions and region2 in regions:
            if region2 not in neighbors[region1]:
                neighbors[region1].append(region2)
            if region1 not in neighbors[region2]:
                neighbors[region2].append(region1)
    return neighbors

neighbors = determine_neighbors(vor, regions)

# Function to draw the map
def draw_map():
    screen.fill(BACKGROUND_COLOR)
    for region, details in regions.items():
        if details['points']:
            points = [(int(x), int(y)) for x, y in details['points']]  # Convert float to int for pygame.draw.polygon
            pygame.draw.polygon(screen, details['color'], points)
            pygame.draw.polygon(screen, LINE_COLOR, points, 3)  # Draw boundary with a line width of 3
            font = pygame.font.Font(None, 36)
            text = font.render(region, True, (0, 0, 0))
            text_rect = text.get_rect(center=(np.mean([p[0] for p in points]), np.mean([p[1] for p in points])))
            screen.blit(text, text_rect)

    pygame.display.update()

# TODO: Implement the remove_inconsistent_values function
def remove_inconsistent_values(xi, xj):
    revised = False
    original_domain_xi = color_domains[xi][:]
    # TODO: Iterate over each color in the domain of xi
    # TODO: For each color, check if it conflicts with all colors in xj's domain
    # TODO: If a color in xi's domain conflicts with every color in xj's domain, remove it
    return revised  # Return True if the domain of xi was revised

# TODO: Implement the AC-3 algorithm
def apply_ac3():
    # Queue of all arcs
    queue = [(region, neighbor) for region in neighbors for neighbor in neighbors[region]]

    while queue:
        (region, neighbor) = ...  # TODO: Remove and handle the first arc in the queue

        # TODO: Call the function remove_inconsistent_values to reduce the domain of region
        if remove_inconsistent_values(region, neighbor):
            # TODO: Check if domain of region is empty after revision, return False if so

            # TODO: If domain is revised, add all neighboring arcs (n, region) back to the queue, where n is a neighbor of region
            pass
        
    return True  # Return True if AC-3 completes without contradiction

# TODO: Implement the backtracking function
def backtrack(region_index=0):
    # Check if all regions are colored (base case)
    if region_index == len(regions):
        return True  # All regions successfully colored

    region = list(regions.keys())[region_index]
    # TODO: Iterate through each color in the color domain of the region
    for ...
        # TODO: Use is_valid function to check if the current color choice is valid
        if ...
            # TODO: Assign the color to the region and attempt to color the next region
            regions[region]['color'] = ...
            if backtrack(region_index + 1): # Recursively color the next region
                return True
            
            regions[region]['color'] = (128, 128, 128)  # Reset to default color on backtrack

    return False  # No valid color found, backtrack

def is_valid(region, color):
    for neighbor in neighbors[region]:
        if 'color' in regions[neighbor] and regions[neighbor]['color'] == colors[color]:
            return False
    return True

# Update region colors based on the reduced domains after applying AC-3
def update_colors():
    for region, domain in color_domains.items():
        if len(domain) == 1:
            regions[region]['color'] = colors[domain[0]]

# Main game loop
running = True
finished = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Apply AC-3
    if apply_ac3():
        update_colors()  # Update colors based on reduced domains
    else:
        print("AC-3 could not reduce domains sufficiently. Starting backtracking...")

    # Start backtracking if AC-3 wasn't enough
    if not all(len(domain) == 1 for domain in color_domains.values()) and not finished:
        if backtrack():
            print("Solution found via backtracking.")
            finished = True
        else:
            print("No solution found via backtracking. Press any key to exit.")
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        pygame.quit()
                        sys.exit()
                pygame.display.update()
                clock.tick(FPS)
            break

    # Draw the map
    draw_map()

    # Maintain frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()
