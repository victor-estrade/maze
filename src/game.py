# -*- coding: utf-8 -*-
import logging


class Game():
    def __init__(self, env, agent):
        self.env = env
        self.agent = agent
        self.reward_log = []
        self.observation_log = []
        self.action_log = []

    def reset(self):
        self.env.reset()
        self.reward_log = []
        self.action_log = []
        self.observation_log = []

    def play(self):
        logger = logging.getLogger(__name__)
        logger.info("Start Game")
        self.env.render()

        done = False
        observation = self.env.state
        reward = 0
        while not done:
            self.env.render()
            action = self.agent.play(observation, reward)
            observation, reward, done = self.env.step(action, observation)
            self.action_log.append(action)
            self.reward_log.append(reward)
            self.observation_log.append(observation)
            logger.info(f"action = {action}, reward = {reward}, observation = {observation}")
