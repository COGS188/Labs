import pygame
import numpy as np
import sys
import argparse
np.random.seed(0)

parser = argparse.ArgumentParser(description="Play the slot machine simulator in manual or AI mode.")
parser.add_argument("--mode", type=str, choices=["manual", "AI"], default="manual",
                    help="Choose 'manual' to play the game yourself or 'AI' for the epsilon-greedy algorithm to play.")
args = parser.parse_args()

# Initialize Pygame
pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Slot Machine Simulator")

# Colors
background_color = (30, 30, 30)
button_color = (100, 200, 100)
text_color = (255, 255, 255)
highlight_color = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Slot machine settings
n_machines = 3
true_rewards = np.random.rand(n_machines) * 0.9 + 0.1  # Random rewards between 0.1 and 1.0
estimated_rewards = np.zeros(n_machines)
play_counts = np.zeros(n_machines)

# Cost and Rewards
cost_per_play = 0.05
total_reward = 0

# Epsilon for exploration
epsilon = 0.1

# Button dimensions
button_width = 150
button_height = 90
button_margin = 30
start_x = (screen_width - n_machines * button_width - (n_machines - 1) * button_margin) / 2

# Game loop
running = True
while running:
    screen.fill(background_color)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and args.mode == "manual":
            pos = pygame.mouse.get_pos()
            for i in range(n_machines):
                x = start_x + i * (button_width + button_margin)
                y = (screen_height - button_height) / 2
                if x <= pos[0] <= x + button_width and y <= pos[1] <= y + button_height:
                    reward = np.random.rand() < true_rewards[i]
                    play_counts[i] += 1
                    total_reward += reward - cost_per_play
                    # TODO: Update estimated_rewards for the chosen machine


    # AI mode action
    if args.mode == "AI":
        # TODO: Implement epsilon-greedy selection of the machine

        # TODO: Simulate obtaining a reward from the chosen machine

        # TODO: Update play_counts and total_reward appropriately
        # Hint: Don't forget to consider the cost_per_play

        # TODO: Update estimated_rewards for the chosen machine using the incremental update formula

        pygame.time.wait(500)

    # Draw buttons and labels
    for i in range(n_machines):
        x = start_x + i * (button_width + button_margin)
        y = (screen_height - button_height) / 2
        pygame.draw.rect(screen, button_color, (x, y, button_width, button_height))
        
        machine_label = font.render(f'Machine {i+1}', True, text_color)
        machine_rect = machine_label.get_rect(center=(x + button_width / 2, y + button_height / 3))
        screen.blit(machine_label, machine_rect)

        plays_label = font.render(f'Plays: {int(play_counts[i])}', True, text_color)
        plays_rect = plays_label.get_rect(center=(x + button_width / 2, y + 2 * button_height / 3))
        screen.blit(plays_label, plays_rect)

    # Display total reward
    reward_text = font.render(f'Net Reward: {total_reward:.2f}', True, text_color)
    reward_rect = reward_text.get_rect(center=(screen_width / 2, 50))
    screen.blit(reward_text, reward_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
