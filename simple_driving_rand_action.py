#!/usr/bin/env python3

import gym
import simple_driving
import time

if __name__ == '__main__':
    env = gym.make('SimpleDriving-v0')
    obs = env.reset()
    for _ in range(1000):
        obs, reward, done, info = env.step(env.action_space.sample())
        time.sleep(0.1)
        if done:
            break
        env.render()
    env.close()
