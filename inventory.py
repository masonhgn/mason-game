import pygame as p
from item import item, items
inv = p.image.load('items/inventory.png')
class inventory(object):
    def __init__(self,x, y, isOpen, isFull):
        self.isOpen = False
        self.isFull = False
        self.x = x
        self.y = y
        self.invent = []

    def draw(self, w):
        if self.isOpen:
            w.blit(inv, (self.x, self.y))
            if len(self.invent) < 10:
                for i in self.invent:
                    itemInvX=2
                    itemInvY=370
                    w.blit(items[i], (itemInvX, itemInvY))
                    itemInvX+=45
                    print(itemInvX, " ", itemInvY)
                

    def open(self):
        self.x -= 900

    def close(self):
        self.x += 900
        
    def addItem(self, item):
        self.invent.append(item.item_id)