import os
import pygame
import sys

BASE_IMG_PATH = 'data/images/'

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def toggle_fullscreen(game):
    game.fullscreen = not game.fullscreen
    if game.fullscreen:
        game.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        print(game.screen.get_size())
    else:
        game.screen = pygame.display.set_mode(game.windowed_size)
        actual_size = game.screen.get_size()
        if actual_size != game.windowed_size:
            print("WARNING: Actual window size does not match desired size.")

def load_image(path):
    img = pygame.image.load(resource_path(BASE_IMG_PATH + path)).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(resource_path(BASE_IMG_PATH + path))):
        images.append(load_image(path + '/'+ img_name))
    return images

class Animation:
    def __init__(self, images, img_dur=5, loop=True):
        self.images = images
        self.loop = loop
        self.img_duration = img_dur
        self.done = False
        self.frame = 0
    
    def copy(self):
        return Animation(self.images, self.img_duration, self.loop)

    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1)
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True 

    def img(self):
        return self.images[int(self.frame / self.img_duration)]

