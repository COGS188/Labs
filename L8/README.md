# Assignment + Lab 8: Eligility Traces + Neural Networks for Reinforcement Learning (10 points)

**Deadline**: Wednesday, June 05, 2024 at 11:59pm on Gradescope

## Installations

For Part 1, you will need the following libraries:

* PyGame
* NumPy
* Argparse
* Tqdm
* Pickle

For Part 2, you will need the following additional libraries:

* Swig
* Gymnasium
* PyTorch

The environment used in Part 2 is the LunarLander-v2 environment from Gymnasium, which requires `box2d` as a dependency. This, in turn, requires `swig` to be installed on your system. You can install these using the following command:

```bash
pip install swig
pip install box2d-py
```

**Note:** If you have difficulties with installing PyTorch and/or Swig and box2d, do not worry because I have created a Google Colab notebook for Part 2 that you can use to complete the assignment.


## Part 1: Eligibility Traces in a Maze Environment [2.5 points]

Eligibility traces are a mechanism in reinforcement learning that bridges the gap between Monte Carlo methods and temporal difference (TD) methods. They allow for more efficient learning by maintaining a trace of visited states and actions, enabling updates not just for the current state-action pair but also for previous ones. Eligibility traces can be implemented in two ways: forward and backward.

### Mathematical Formulation

**Forward Eligibility Traces:**
The forward view of eligibility traces involves updating the state-action values (Q-values) over multiple steps. The key idea is to accumulate a weighted sum of TD errors over time.

For a given state \(s_t\) and action \(a_t\):

1. Initialize \(e(s, a) = 0\) for all \(s\) and \(a\).
2. For each time step \(t\):
    - Choose action \(a_t\) using an epsilon-greedy policy.
    - Observe reward \(r_{t+1}\) and next state \(s_{t+1}\).
    - Choose next action \(a_{t+1}\) using an epsilon-greedy policy.
    - Compute the TD error: \(\delta_t = r_{t+1} + \gamma Q(s_{t+1}, a_{t+1}) - Q(s_t, a_t)\).
    - Update the eligibility trace: \(e(s_t, a_t) += 1\).
    - For all state-action pairs \((s, a)\):
      $$Q(s, a) \leftarrow Q(s, a) + \alpha \delta_t e(s, a)$$ $$e(s, a) \leftarrow \gamma \lambda e(s, a)$$

**Backward Eligibility Traces:**
The backward view updates the Q-values and eligibility traces immediately after each step. It adjusts the traces and Q-values using the TD error.

For a given state \(s_t\) and action \(a_t\):

1. Initialize \(e(s, a) = 0\) for all \(s\) and \(a\).
2. For each time step \(t\):
    - Choose action \(a_t\) using an epsilon-greedy policy.
    - Observe reward \(r_{t+1}\) and next state \(s_{t+1}\).
    - Compute the TD error: \(\delta_t = r_{t+1} + \gamma \max_{a} Q(s_{t+1}, a) - Q(s_t, a_t)\).
    - Update the eligibility trace: \(e(s_t, a_t) += 1\).
    - For all state-action pairs \((s, a)\):
      $$Q(s, a) \leftarrow Q(s, a) + \alpha \delta_t e(s,a)$$ $$e(s, a) \leftarrow \gamma \lambda e(s, a)$$

### Running the Code

You are provided with the starter code in `eligibility_traces_maze.py` that sets up the maze environment and the structure for implementing eligibility traces. Your task is to complete the `TODO` sections in the code. The maze environment is identical to that used in L2, when you implemented A* and simulated annealing.

To run the script using forward eligibility traces, use the following command:

```bash
python eligibility_traces_maze.py forward
```

To run the script using backward eligibility traces, use the following command:

```bash
python eligibility_traces_maze.py backward
```

### Tasks to Complete

1. Epsilon-Greedy Policy: Implement the epsilon-greedy policy in the `choose_action` function to select an action from the action space.
2. Reward Function: Implement the reward function in the `get_reward` function to return the appropriate reward for reaching the given state. The definition of the reward function is up to you, but it should encourage the agent to reach the goal state.
3. Forward Eligibility Traces Update: Complete the `update` method in the `ForwardEligibilityTraces` class to implement the update rule for forward eligibility traces.
4. Backward Eligibility Traces Update: Complete the `update` method in the `BackwardEligibilityTraces` class to implement the update rule for backward eligibility traces.
5. Training Loop for Forward Eligibility Traces: Implement the training loop in the `train` method of the `ForwardEligibilityTraces` class.
6. Training Loop for Backward Eligibility Traces: Implement the training loop in the `train` method of the `BackwardEligibilityTraces` class.

For tasks 5 and 6, you may use the `tqdm` library to display a progress bar during training. 

Once you have completed the code, run the script using the commands provided above to visualize the resulting paths taken by the agent in the maze environment. 

Once you are done, take a screenshot of the maze environment with the agent's path for both forward and backward eligibility traces. Save these screenshots as `forward.png` and `backward.png` respectively.

### Optional Task: Saving the Trained Model

You might observe that, everytime you click on the "New Map" button, the agent has to retrain from scratch. This can be time-consuming, especially for larger mazes. To address this issue, you can save the trained model after training and load it when needed. As an optional challenge, learn how to use the `pickle` library in Python to save and load the trained model for both forward and backward eligibility traces. Once you've implemented this functionality, save the trained models as `forward_trained_model.pkl` and `backward_trained_model.pkl`, and load them when running the script so that the same model can be used for different maze environments.

## Part 2: Neural Networks for Reinforcement Learning [2.5 points]

For this part of the assignment, we'll be using the LunarLander-v2 environment from Gymnasium. The goal of the agent is to land the lunar module on the landing pad within the environment. The agent receives a reward for moving the lander from the top of the screen to the landing pad and zero speed. The agent also receives a reward for landing the lander safely on the landing pad. The episode ends if the lander crashes or comes to rest, and the environment provides additional rewards for landing within the landing pad and moving closer to the center of the pad.

For more details on the LunarLander-v2 environment, refer to the [Gymnasium documentation](https://www.gymlibrary.dev/environments/box2d/lunar_lander/).

To get an intuitive feel for how this environment works, you can run the following code:

```python
python lunar_lander_keyboard.py
```

The code in that file is very simple and allows you to control the spaceship using the arrow keys on your keyboard. The goal is to land the spaceship on the landing pad (in between the two flags) without crashing. I recommend you try playing around with it for a bit to get a feel for how the environment works, and what the rewards are.

**Warning:** It's pretty hard to land the spaceship using the keyboard, so don't worry if you crash a lot! If you can't get it to land after a few tries, I'd recommend moving on. (You'll probably realize that it's easier to train a neural network to solve this task than to do it yourself!)

In this part, you will implement a Deep Q-Network (DQN) to solve the Lunar Lander environment from the Gymnasium library. The goal of the assignment is to provide hands-on experience with reinforcement learning and neural networks. You will complete the implementation of a DQN agent, including the neural network, experience replay, and training loop.

The starter code can be found in `lunar_lander_dqn.py`. 

If you are unable to get the installations to work on your local machine, you can use the Google Colab notebook at this link: https://colab.research.google.com/drive/1kztw2-2BCtYQZZW_8Pg804ioFGJlCwlb?usp=sharing

The code is divided into several sections:

* `QNetwork` Class: Define the neural network architecture and forward pass.
* `ReplayBuffer` Class: Implement a fixed-size buffer to store experience tuples and sample batches of experiences for training.
* `DQNAgent` Class: Implement the DQN agent, including methods for interacting with the environment, storing experiences, and learning from them.
* `dqn` Function: Implement the main training loop for the DQN agent.
* Plotting and Video Generation: Plot the training progress and create a video of the trained agent's performance.

### Tasks to Complete

#### `QNetwork` Class

The `QNetwork` class defines the neural network used to approximate the Q-values for each action. You will:

* Define the neural network layers in the `__init__` method.
* Implement the forward pass in the forward method.
  
#### `ReplayBuffer` Class

The `ReplayBuffer` class implements a fixed-size buffer to store experience tuples. You will:

* Implement the `add` method to add new experiences to the memory.
* Implement the `sample` method to randomly sample a batch of experiences from the memory.

#### `DQNAgent` Class

The DQNAgent class interacts with the environment and learns from experiences. You will:

* Initialize Q-networks (local and target) and the replay buffer in the `__init__` method.
* Implement the `step` method to save experiences in the replay buffer and periodically sample a batch to learn from.
* Implement the `act` method to select actions based on an epsilon-greedy policy.
* Implement the `learn` method to update the Q-networks using a batch of experiences.
* Implement the `soft_update` method to update the target network parameters.

#### `dqn` Function

The dqn function implements the main training loop. You will:

* Initialize the environment and agent.
* Implement the training loop to interact with the environment, collect experiences, and update the agent.
* Save the trained model when the environment is solved.

#### Plotting and Video Generation

* Use the `plot_scores` function to visualize the training progress.
* Use the `create_video` function to generate a video of the trained agent's performance.

#### Hyperparameters

You can experiment with different hyperparameters to improve the agent's performance. Some hyperparameters you can tune include:

* Learning rate
* Discount factor (gamma)
* Batch size
* Replay buffer size
* Epsilon start, end, and decay rate

You are also welcome to tweak the architecture of the neural network to see if you can improve the agent's performance.

The `TODO` sections in the code indicate where you need to complete the implementation. Once you have completed the code, run the script using the following command:

```bash
python lunar_lander_dqn.py
```

**Note:** I've gotten the training to work pretty fast using a CPU, so I don't think it's necessary to use a GPU for this assignment. However, if you feel it's too slow, you can try running it on a GPU.

This will train the DQN agent to solve the Lunar Lander environment. The training progress will be displayed, and a video of the trained agent's performance will be saved as `lunar_lander.mp4`.

Furthermore, a plot of the training progress will be displayed, showing the scores obtained during training. The plot should show the scores increasing over time as the agent learns to land the lunar module successfully. You will expect to see some noise in the scores due to the stochastic nature of the environment and the exploration strategy, but that is perfectly normal. The resulting plot will be saved to `training_scores.png`.

When you open the video, you should see the agent successfully landing the lunar module on the landing pad. The agent should land slowly and safely, avoiding crashes and coming to rest within the landing pad.

## Part 3: Comparing Different Methods [2.5 points]

In this class, you've learned several different algorithms for reinforcement learning, such as Q-learning, SARSA, Monte Carlo Methods, Eligibility Traces, and Deep Q-Networks. For this part of the assignment, you will compare the performance of these algorithms on the Lunar Lander environment from Gymnasium.

You've already implemented Q-learning and SARSA in Lab 7 and Monte Carlo Methods in Lab 6. You are free to reuse the code from those labs for this part of the assignment. Furthermore, if you were unable to complete any of the previous labs, you can use the provided solutions on Canvas to help you with the code.

### Tasks to Complete

* Implement **two** additional RL algorithms on the **Lunar Lander environment**. Choose any two out of the following three options:
  * Q-learning
  * SARSA
  * Monte Carlo Methods (any method you like, such as First-Visit, Every-Visit, On-Policy, Off-Policy, etc.)
  * Eligibility Traces (either forward or backward, but don't pick both of these as your two additional algorithms)

* Evaluate the algorithms based on the following performance metrics. Choose any **two** out of the following four options, or come up with your own metrics (as long as they are reasonable and informative):
  * Average Reward: The average reward obtained per episode over a fixed number of episodes (e.g., 100 episodes).
  * Convergence Rate: The number of episodes required for the algorithm to converge to a stable policy.
  * Stability: The variance in the rewards over time, indicating how consistently the algorithm performs once it has converged.
  * Computation Time: The total time taken to train the algorithm until convergence.
* Prepare a short report (maximum 5 pages) summarizing your comparative analysis. The report should include:
  * **Introduction**: Briefly introduce the three RL algorithms you implemented.
  * **Methodology**: Explain how you implemented each algorithm. Describe how you collected the performance metrics.
  * **Results**: Present the performance metrics for each algorithm using tables and graphs. Compare the algorithms based on the metrics.
  * **Discussion**: Discuss the strengths and weaknesses of each algorithm. Explain any interesting observations from your results.
  * **Conclusion**: Summarize your findings. Provide insights into the applicability of different RL algorithms to complex environments like Lunar Lander.
  * **Instructions**: Include instructions on how to run your code to reproduce the results.

Submit your report as a PDF file named `report_part3.pdf`.

## Part 4: Exploring RL in Stable Baselines [2.5 points]

In the final part of the assignment, you will use the Stable-Baselines3 library to explore, implement, and compare different reinforcement learning (RL) algorithms across multiple environments. You will also perform an ablation study to analyze the impact of different hyperparameters on the performance of these algorithms.

First, you can install Stable-Baselines3 using pip:

```bash
pip install stable-baselines3
```

Here is the GitHub repository for Stable-Baselines3: https://github.com/DLR-RM/stable-baselines3

The repository contains detailed documentation on how to use the library, including examples and tutorials for different RL algorithms. I recommend running the examples provided in the repository to get familiar with the library.

### Tasks to Complete

#### Step 1: Choose Environments and Algorithms

Choose **at least two** different environments from Gymnasium **that we haven't used before in the labs**. Some interesting options include:

* CartPole-v1
* Acrobot-v1
* Pendulum-v0

Choose **at least three** different RL algorithms from Stable-Baselines3. Some popular choices are:

* A2C (Advantage Actor-Critic)
* PPO (Proximal Policy Optimization)
* DQN (Deep Q-Network)
* SAC (Soft Actor-Critic)
* TD3 (Twin Delayed DDPG)

We haven't covered these algorithms in class, but the goal of this assignment is to explore new algorithms and environments. You can refer to the [Stable-Baselines3 documentation](https://stable-baselines3.readthedocs.io/en/master/) for more information on these algorithms.

#### Step 2: Implement and Train the Algorithms

Using the provided starter code for DQN as a reference, implement and train the selected algorithms on the chosen environments. Ensure that your implementations can be executed in each environment. 

#### Step 3: Evaluate and Compare the Algorithms

Evaluate the performance of each model using the following metrics:

* Average Reward: The average reward obtained per episode over a fixed number of episodes (e.g., 100 episodes).
* Convergence Rate: The number of timesteps required for the algorithm to converge to a stable policy.
* Stability: The variance in the rewards over time, indicating how consistently the algorithm performs once it has converged.
* Computation Time: The total time taken to train the algorithm until convergence.

#### [Optional] Step 4: Perform an Ablation Study

An ablation study involves systematically varying different hyperparameters of the algorithms to analyze their impact on performance. You can experiment with different hyperparameters such as learning rate, discount factor, batch size, etc., and observe how they affect the training process and final performance. 

#### Step 5: Prepare a Report

Prepare a short report (maximum 5 pages) summarizing your findings. The report should include:

* **Introduction**: Briefly introduce the selected environments and algorithms.
* **Methodology**: Explain how you implemented and trained each algorithm. Describe how you collected the performance metrics.
* **Results**: Present the performance metrics for each algorithm using tables and graphs. Compare the algorithms based on the metrics.
* **Discussion**: Discuss the strengths and weaknesses of each algorithm. Explain any interesting observations from your results.
* **Conclusion**: Summarize your findings. Provide insights into the applicability of different RL algorithms to various environments.
* **Instructions**: Include instructions on how to run your code to reproduce the results.
* **References**: Include any references or resources you used for the assignment, such as the Stable-Baselines3 documentation.

Submit your report as a PDF file named `report_part4.pdf`.

## Submission Instructions

Submit the following files to Gradescope:

1. Part 1:
   1. `forward.png`
   2. `backward.png`
   3. `eligibility_traces_maze.py`
   4. [Optional] `forward_trained_model.pkl`
   5. [Optional] `backward_trained_model.pkl`
2. Part 2:
   1. `lunar_lander_dqn.py` (or the Jupyter notebook if you used Google Colab)
   2. `lunar_lander_keyboard.py`
   3. `training_scores.png`
   4. `lunar_lander.mp4`
   5. `checkpoint.pth`
3. Part 3:
   1. `report_part3.pdf`
   2. Any additional code for the two additional RL algorithms. (If you keep all the code in one file, that's fine too.)
   3. Any additional files needed to run the code / any images you want to show in the report.
4. Part 4:
   1. `report_part4.pdf`
   2. Any additional code for the selected environments and algorithms.
   3. Any additional files needed to run the code / any images you want to show in the report.

Make sure to save your Python files before uploading them. You can submit as many times as you like before the deadline. Only the last submission will be graded.