import matplotlib.pyplot as plt
import random
import math
from matplotlib.animation import FuncAnimation

def estimate_pi(num_samples, step=100):
    """
    Estimate the value of Pi using the Monte Carlo method by simulating random point placements.

    Parameters:
        num_samples (int): Total number of random points to generate.
        step (int): Frequency of data collection for animation frames.

    Returns:
        data: list of tuples: Each tuple contains:
                        - List of x-coordinates inside the circle.
                        - List of y-coordinates inside the circle.
                        - List of x-coordinates outside the circle.
                        - List of y-coordinates outside the circle.
                        - Current Pi estimate.

    This format is chosen to facilitate easy auto-grading and analysis.
    """
    inside_circle = 0
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []
    data = []

    # TODO: Implement the Monte Carlo simulation to estimate Pi
    # Add your code here

    # Note that the data gets populated every 'step' samples

    return data # this should be a list of tuples as described in the docstring


def create_animation(num_samples):
    data = estimate_pi(num_samples)
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.axis('equal')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    
    scat_inside = ax.scatter([], [], color='blue', s=1, label='Inside Circle')
    scat_outside = ax.scatter([], [], color='red', s=1, label='Outside Circle')
    title = ax.set_title("")
    ax.legend(loc='upper right')

    def update(frame):
        x_inside, y_inside, x_outside, y_outside, pi_estimate = frame
        scat_inside.set_offsets(list(zip(x_inside, y_inside)))
        scat_outside.set_offsets(list(zip(x_outside, y_outside)))
        title.set_text(f"Estimation of Pi after {len(x_inside) + len(x_outside)} Samples: Pi ≈ {pi_estimate:.4f}")

    animation = FuncAnimation(fig, update, frames=data, interval=50)
    animation.save('monte_carlo_pi.gif', writer='imagemagick')
    plt.close(fig)

# Set the number of samples and the step for frames
num_samples = 10000
create_animation(num_samples)
