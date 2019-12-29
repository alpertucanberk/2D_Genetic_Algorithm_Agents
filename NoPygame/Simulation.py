
import numpy as np
import sys
import time

sys.path.insert(1, './Sprites')
from Utils import *

import matplotlib.pyplot as plt
plt.ion()

class Simulation():

    def __init__(self, screen_width, screen_height, type_dict):

        self.display = np.zeros((screen_width, screen_height))
        self.all_sprites = []

        clear_log()

        log("screen_size")
        log("width", screen_width)
        log("height", screen_height)

        log("type dict:")
        for key in type_dict.keys():
            log(type_dict[key], key)

        self.visualize=False

    def add_sprite(self, object):
        self.all_sprites.append(object)

    def render_screen(self):

        for sprite in self.all_sprites:
            sprite.render(self.display)

        if self.visualize:
            plt.close()
            plt.matshow(self.display)
            plt.show()
            plt.pause(0.001)

    def update_sprites(self):
        for sprite in self.all_sprites:
            sprite.update()

    def run(self, num_steps, visualize = False):

        if visualize:
            self.visualize = True

        for i in range(0, num_steps):
            print("Frame", i)
            self.render_screen()
            self.update_sprites()
            if not (i == num_steps):
                self.display = np.zeros((self.display.shape[0], self.display.shape[1]))
            log("Frame", i)

    def get_fitness(self, type):
        return [agent.fitness_metric() for agent in self.all_sprites if agent.type == type]
