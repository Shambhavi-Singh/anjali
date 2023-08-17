import os
import sys

# sys.path.append(os.path.dirname(os.path.abspath(__file__)) +
#                 "/../../Sampling_based_Planning/")

import plotting

terrains_dict = {1:"Chaos Terrain", 2:"Mesas Terrain", 3:"Cliffs Terrain", 4:"Craters Terrain", 5:"Glacier Terrain", 6:"Sand Dunes Terrain", 7:"Gullies Terrain", 8:"Medusae Fossae Terrain", 9:"Scalloped Terrain", 10:"Mud Volcanic Terrain", 11: "Random 1", 12:"Random 2", 13: "Random 3"}

def main():
    plot = plotting.Plotting((2,2), (49,24))
    plot.animation([], [], terrains_dict[plotting.env.terrain])

if __name__ == '__main__':
    main()