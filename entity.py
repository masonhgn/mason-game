import pygame as p

mobs = [p.image.load('player_sprites/mob.png')]
solid = [p.image.load('environment/stonewall.png'), p.image.load('environment/rock.png'), p.image.load('environment/tree.png')]

class entity(object):


    def __init__(self, spawnx, spawny, x,y, level, health, name, entity_type):
        self.entity_type = ['mob', 'solid']
        self.name = name
        self.x=x
        self.y=y
        self.spawnx = spawnx
        self.spawny= spawny
        self.velocity=5
        self.level = level
        self.health = health
        self.dead = False

    def __str__(self):
        return self.name

    #if (self.entity_type == 'solid'):
        #if (m.x - 128 == self.x) and (m.y - 128 == self.y):
            #print("collision")


    def draw(self, w):

        if self.name == 'monster':
            w.blit(mobs[0], (self.x, self.y))
        if self.name == 'rock':
            w.blit(solid[1], (self.x, self.y))
        if self.name == 'tree':
            w.blit(solid[2], (self.x, self.y))
        if self.name == 'stonewall':
            w.blit(solid[0], (self.x, self.y))


        #w.blit(mob, (self.x,self.y))

    def printCoords(self):
        print('x: ' , (-1*(m.x - monster.x) - 3600) - 300, " y: ", ((-1*(m.y - monster.y) - 3700) - 300)*-1)
    

    def pace(self):
        reachedRight = False
        reachedLeft = False

        if not reachedRight:
            self.x += self.velocity/10
            if self.x >= (self.spawnx + 100):
                reachedRight = True        
        if reachedRight:
            self.velocity *= -1
        if self.x <= (self.spawnx - 100):
            reachedLeft = True

        if reachedLeft:
            self.velocity*=-1   
    def stop(self):
        self.velocity = 0

    def followPlayer(self, player):

        

        #if (abs(ogre.x - monster.x)) < 160 or (abs(ogre.y - monster.y)) < 160:
           # monster.attackPlayer()

        #if monster is left of player, close enough, but not too close
        if self.x < player.x - 128 and self.x > player.x - 400:
            self.velocity = 5
            self.x += self.velocity
        #if monster is right of player, close enough, but not too close
        elif self.x > player.x + 128 and self.x < player.x + 400:
            self.velocity = -5
            self.x += self.velocity
        #if monster is south of player, close enough, but not too close
        if self.y < player.y - 128 and self.y > player.y - 400:
            self.velocity = 5
            self.y += self.velocity
        #if monster is north of player, close enough, but not too close
        elif self.y > player.y + 128 and self.y < player.y + 400:
            self.velocity = -5
            self.y += self.velocity

    def attackPlayer(self, player):
        def hitPlayer():
            if player.health > 0:
                player.sethealth(player.health - 1)
            else:
                player.death()
        t=threading.Timer(5.0,hitPlayer)
        t.start()