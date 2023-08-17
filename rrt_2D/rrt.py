import os
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


sys.path.append(os.path.dirname(os.path.abspath(__file__)) +
                "/../../Sampling_based_Planning/")



class Node:
    def __init__(self, n):
        self.x = n[0]
        self.y = n[1]
        self.parent = None

import env, plotting, utils, timer

class Rrt:
    def __init__(self, s_start, s_goal, step_len, goal_sample_rate, iter_max):
        self.s_start = Node(s_start)
        self.s_goal = Node(s_goal)
        self.step_len = step_len
        self.goal_sample_rate = goal_sample_rate
        self.iter_max = iter_max
        self.vertex = [self.s_start]

        self.env = env.Env()
        self.plotting = plotting.Plotting(s_start, s_goal)
        self.utils = utils.Utils()

        self.x_range = self.env.x_range
        self.y_range = self.env.y_range
        self.obs_circle = self.env.obs_circle
        self.obs_rectangle = self.env.obs_rectangle
        self.obs_boundary = self.env.obs_boundary

    def planning(self):
        for i in range(self.iter_max):
            node_rand = self.generate_random_node(self.goal_sample_rate)
            node_near = self.nearest_neighbor(self.vertex, node_rand)
            node_new = self.new_state(node_near, node_rand)

            if node_new and not self.utils.is_collision(node_near, node_new):
                self.vertex.append(node_new)
                dist, _ = self.get_distance_and_angle(node_new, self.s_goal)

                if dist <= self.step_len and not self.utils.is_collision(node_new, self.s_goal):
                    self.new_state(node_new, self.s_goal)
                    return self.extract_path(node_new)

        return None

    def generate_random_node(self, goal_sample_rate):
        delta = self.utils.delta

        if np.random.random() > goal_sample_rate:
            return Node((np.random.uniform(self.x_range[0] + delta, self.x_range[1] - delta),
                         np.random.uniform(self.y_range[0] + delta, self.y_range[1] - delta)))

        return self.s_goal

    @staticmethod
    def nearest_neighbor(node_list, n):
        return node_list[int(np.argmin([math.hypot(nd.x - n.x, nd.y - n.y)
                                        for nd in node_list]))]

    def new_state(self, node_start, node_end):
        dist, theta = self.get_distance_and_angle(node_start, node_end)

        dist = min(self.step_len, dist)
        node_new = Node((node_start.x + dist * math.cos(theta),
                         node_start.y + dist * math.sin(theta)))
        node_new.parent = node_start

        return node_new

    def extract_path(self, node_end):
        path = [(self.s_goal.x, self.s_goal.y)]
        node_now = node_end

        while node_now.parent is not None:
            node_now = node_now.parent
            path.append((node_now.x, node_now.y))

        return path

    @staticmethod
    def get_distance_and_angle(node_start, node_end):
        dx = node_end.x - node_start.x
        dy = node_end.y - node_start.y
        return math.hypot(dx, dy), math.atan2(dy, dx)


def main(start=(2,2), goal=(49,24), terrain=1, analysis=False, iterations=1, n=10000):
    x_start = start  # Starting node
    x_goal = goal  # Goal node
    env.terrain = terrain
    time = timer.Timer()
    
    if analysis:
        # For analysis
        elapsed_time = []
        path_len = []
        path_count = []
        for i in range(iterations):
            rrt = Rrt(x_start, x_goal, 0.5, 0.05, n)
            time.start()
            path = rrt.planning()
            time.stop()
            elapsed_time.append(time.elapsed_time)
            path_len.append(rrt.utils.path_length(path))
            path_count.append(len(path) if path else 0)
            # print(time.elapsed_time)

        fig = rrt.plotting.animation(rrt.vertex, path, "RRT", True)
        print("elapsed_time: ")
        for i in elapsed_time:
            print(i)

        print ("path length: ")
        for i in path_len:
            print(i)

        print ("path nodes: ")
        for i in path_count:
            print(i)
    
    else:
        # Main demo part
        rrt = Rrt(x_start, x_goal, 0.5, 0.05, n)
        time.start()
        path = rrt.planning()
        time.stop()
        print(time)    
        if path:
            print("Path Length:", rrt.utils.path_length(path))
            print("Path Nodes: ", len(path))
            fig = rrt.plotting.animation(rrt.vertex, path, "RRT", True)
        else:
            print("No Path Found!")

    return fig



if __name__ == '__main__':
    main()
