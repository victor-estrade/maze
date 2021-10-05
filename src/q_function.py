# -*- coding: utf-8 -*-

from src.action import Action

class Qfunction():
    def __init__(self, world, policy, gamma=1):
        self.world = world
        self.policy = policy
        self.gamma = gamma

    def q_value(self, action, state):
        old_cumulative_reward = self.world.cumulative_reward
        old_state = self.world.state

        self.world.state = state
        observation = state
        done = False
        move = action
        all_rewards = []
        while not done:
            observation, reward, done = self.world.step(move, observation)
            move = self.policy.next_move(observation)
            all_rewards.append(reward)
        value = self.gamma_cumulative(all_rewards)

        self.world.cumulative_reward = old_cumulative_reward
        self.world.state = old_state
        return value

    def __call__(self, action, state):
        return self.q_value(action, state)

    def gamma_cumulative(self, all_rewards):
        cumul = 0
        for reward in all_rewards[::-1]:
            cumul = self.gamma * cumul + reward
        return cumul

    def compute_all_q_value(self):
        q_value_table = {}
        for state in self.world.all_possible_states():
            for action in list(Action):
                q_value_table[(state, action)] = self.q_value(action, state)
        return q_value_table



class TabularQfunction():
    def __init__(self, world, policy, gamma=1):
        self.q_value_table = Qfunction(world, policy, gamma=1).compute_all_q_value()
        self.gamma = gamma

    def q_value(self, action, state):
        return self.q_value_table[(state, action)]

    def __call__(self, action, state):
        return self.q_value(action, state)

    def update_q_value(self, action, sate, new_value):
        self.q_value_table[(state, action)] = new_value
