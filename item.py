import pygame as p

items = [p.image.load('items/coins.png'), p.image.load('items/gloves.png')]

class item(object):
    def __init__(self, item_id, name, x, y):
        self.item_id = item_id
        self.name = name
        self.x = x
        self.y = y
    def draw(self, w):
        
        if self.item_id == 1:
            w.blit(items[0], (self.x, self.y))
        if self.item_id == 2:
            w.blit(items[1], (self.x, self.y))
    def remove(self):
        self.x += 8000
        self.y += 8000


