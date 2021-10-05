# -*- coding: utf-8 -*-

import numpy as np

from src.action import Action

class RandomAgent():
    def play(self, observation, reward):
        action = np.random.choice(list(Action))
        return action


class PolicyDrivenAgent():
    def __init__(self, policy):
        self.policy = policy

    def play(self, observation, reward):
        move = self.policy.next_move(observation)
        return move
