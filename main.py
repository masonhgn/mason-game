import pygame as p
import os
import time
import threading
from player import player
from entity import entity
from inventory import inventory
from item import item

p.init()
c = p.time.Clock()

entities = []
solids = []
items = []
SCREEN_W = 800
SCREEN_H = 600
w = p.display.set_mode((SCREEN_W, SCREEN_H))
p.display.set_caption("Mason's Game")
collision = False



bg = p.image.load('environment/bg.jpg')
char = p.image.load('player_sprites/standing.png')

class mapp(object):
    def __init__(self,x,y):
        self.x= -3600
        self.y= -3700
        self.velocity = 14
        self.left = False
        self.right = False
        self.standing = True

    def draw(self, w):
        w.blit(bg, (self.x,self.y))
        



def drawGame():
    
    m.draw(w)
    if playerInv.isOpen:
        playerInv.x = 0
        playerInv.y = SCREEN_H - 233
    else:
        playerInv.x = 900


    for obj in items:
        obj.draw(w)

    ogre.draw(w)

    for obj in entities:
        obj.draw(w)
        if obj.name == 'monster':
            obj.followPlayer(ogre)

    playerInv.draw(w)
    p.display.update()




####### main ############
m = mapp(-3600,-3700)
entities.append(entity(-200,600,-200,600,5,10,'monster',entity_type='mob'))
entities.append(entity(100,100,100,100,5,10,'monster', entity_type='mob'))
entities.append(entity(-500,300,-500,300,0,0,'tree', entity_type='solid'))
playerInv = inventory(900, SCREEN_H - 300, False, False)

items.append(item(1,'coins',100,100))
items.append(item(2,'globes',100,100))

ogre = player(400, 300, 64, 64)
####### main ############



run = True

while run:
    c.tick(27)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    
    k = p.key.get_pressed()



    #monster.printCoords()
    
    
    ### left right up down player ####
    if k[p.K_a]:
        for obj in entities:
                obj.x +=m.velocity
                obj.spawnx-=m.velocity

        
        for obj in items:
            obj.x +=m.velocity
        m.x+=m.velocity
        ogre.right = True
        ogre.left = False
        ogre.standing = False


    elif k[p.K_d]:
        for obj in entities:
            obj.x -=m.velocity
            obj.spawnx-=m.velocity

        
        for obj in items:
            obj.x -=m.velocity
        m.x-=m.velocity
        ogre.right = True
        ogre.left = False
        ogre.standing = False


    elif k[p.K_w]:

        for obj in entities:
            obj.y +=m.velocity
            obj.spawny+=m.velocity
        for obj in items:
            obj.y +=m.velocity
        m.y+=m.velocity
        ogre.right = False
        ogre.left = False
        ogre.standing = True

    elif k[p.K_s]:

        for obj in entities:
            obj.y -=m.velocity
            obj.spawny-=m.velocity
        for obj in items:
            obj.y -=m.velocity
        m.y-=m.velocity
        ogre.right = False
        ogre.left = False
        ogre.standing = True

    elif k[p.K_j]:
        #monster.attackPlayer()
        #ogre.death()
        playerInv.addItem(items[0])
        items.append(item(1,'coins',100,100))
        print(playerInv.invent)
    elif k[p.K_b]:
        if playerInv.isOpen:
            time.sleep(0.3)
            playerInv.close()
            playerInv.isOpen = False

        else:
            time.sleep(0.3)
            playerInv.open()
            playerInv.isOpen = True

    else:
        ogre.standing = True
        ogre.walk = 0

    

    drawGame()
    
    
p.quit()