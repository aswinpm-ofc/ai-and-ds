# ============================================================
# Q7: Maze Solving using Q-Learning and Gymnasium
# ============================================================

import gymnasium as gym
from gymnasium import spaces
import numpy as np
import matplotlib.pyplot as plt
import random

# ---------------------------
# Custom Maze Environment
# ---------------------------

class MazeEnv(gym.Env):
    def __init__(self, size=5):
        super(MazeEnv, self).__init__()
        self.size = size
        self.maze = np.zeros((size, size))

        # Walls
        self.maze[1,1] = -1
        self.maze[2,2] = -1
        self.maze[3,1] = -1

        self.start = (0,0)
        self.goal = (size-1, size-1)

        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Discrete(size*size)

        self.reset()

    def reset(self, seed=None, options=None):
        self.state = self.start
        return self._get_state(), {}

    def _get_state(self):
        return self.state[0]*self.size + self.state[1]

    def step(self, action):
        x,y = self.state

        if action == 0: x -= 1
        if action == 1: x += 1
        if action == 2: y -= 1
        if action == 3: y += 1

        if x<0 or y<0 or x>=self.size or y>=self.size:
            x,y = self.state

        if self.maze[x,y] == -1:
            x,y = self.state

        self.state = (x,y)

        reward = -1
        terminated = False

        if self.state == self.goal:
            reward = 100
            terminated = True

        return self._get_state(), reward, terminated, False, {}

# ---------------------------
# Q-Learning
# ---------------------------

env = MazeEnv()
q_table = np.zeros((env.size*env.size, env.action_space.n))

alpha = 0.1
gamma = 0.9
epsilon = 0.1
episodes = 500

rewards = []

for ep in range(episodes):
    state, _ = env.reset()
    total_reward = 0

    done = False
    while not done:
        if random.uniform(0,1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state])

        next_state, reward, done, _, _ = env.step(action)

        q_table[state,action] += alpha * (
            reward + gamma*np.max(q_table[next_state]) - q_table[state,action]
        )

        state = next_state
        total_reward += reward

    rewards.append(total_reward)

print("Training Completed.")

plt.plot(rewards)
plt.title("Learning Curve")
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.savefig("training_rewards.png")
print("Graph saved as training_rewards.png")