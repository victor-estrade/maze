# -*- coding: utf-8 -*-

import numpy as np

from src.action import Action

class RandomAgent():
    def play(self, observation, reward):
        action = np.random.choice(list(Action))
        return action
