import random
import numpy as np
import itertools

CLEAN = 0
DIRTY = 1

DO_NOTHING = -1
MOVE_RIGHT = 0
MOVE_LEFT = 1
SUCK = 3

class Environment:
    def __init__(self, area, size):
        self.area = list(area)
        self.size = size
        #print("area = {}\n".format(self.area))

    #The performance measure awards one point for each clean square at each time step,
    #over a “lifetime” of 1000 time steps. ( 0 is clean, 1 is dirty, size - Sum = number of clean cells)
    def measure_performace (self):
        return self.size - np.sum(self.area);

    def mark_as_clean(self, location):
        self.area[location] = CLEAN
        #print("Location {} is Cleaned = {}".format(location, self.area))
        return

class ReflexAgent:
    def __init__(self, env, initial_location):
        self.performance = 0
        self.env = env
        self.performance = 0
        self.location = initial_location;

    def perceive(self):
        action = DO_NOTHING
        percept = self.env.area[self.location]

        if percept == DIRTY:
            action = SUCK
        elif percept == CLEAN and self.env.size > 1:
            if self.location + 1 == self.env.size:
                action = MOVE_LEFT
            elif self.location == 0:
                action = MOVE_RIGHT
            else:
                action = random.choice([MOVE_RIGHT, MOVE_LEFT])
        return action

    def run(self, steps):
        for step in range(steps):
            action = self.perceive()
            if action == MOVE_LEFT:
                self.location -= 1
            elif action == MOVE_RIGHT:
                self.location += 1
            elif action == SUCK:
                self.env.mark_as_clean(self.location)
            self.performance += self.env.measure_performace()

def measure_performance_of_all_dirt_configuration(area_size, steps):
    count = sum = 0
    for initial_location in range(area_size):
        allDirtConfiguration = itertools.product([0, 1], repeat=area_size)
        for conf in list(allDirtConfiguration):
            env = Environment(conf, area_size)
            agent = ReflexAgent(env, initial_location)
            agent.run(steps)
            print("Initial Location {}, area {}, Final Performance: {}".format(initial_location,conf, agent.performance))
            sum+=agent.performance
            count+=1
    print("averge score: {}".format(sum/count))

measure_performance_of_all_dirt_configuration(2,1000)