import pygame as p


health = [p.image.load('health/h0.png'), p.image.load('health/h1.png'), p.image.load('health/h2.png'), p.image.load('health/h3.png'), p.image.load('health/h4.png'), p.image.load('health/h5.png'), p.image.load('health/h6.png'), p.image.load('health/h7.png'), p.image.load('health/h8.png'), p.image.load('health/h9.png'), p.image.load('health/h10.png'),]
walkRight = [p.image.load('player_sprites/r1.png'), p.image.load('player_sprites/r2.png'), p.image.load('player_sprites/r3.png'), p.image.load('player_sprites/r4.png'), p.image.load('player_sprites/r5.png'), p.image.load('player_sprites/r6.png'), p.image.load('player_sprites/r7.png'), p.image.load('player_sprites/r8.png'), p.image.load('player_sprites/r9.png')]
walkLeft = [p.image.load('player_sprites/l1.png'), p.image.load('player_sprites/l2.png'), p.image.load('player_sprites/l3.png'), p.image.load('player_sprites/l4.png'), p.image.load('player_sprites/l5.png'), p.image.load('player_sprites/l6.png'), p.image.load('player_sprites/l7.png'), p.image.load('player_sprites/l8.png'), p.image.load('player_sprites/l9.png')]


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 14
        self.j = False
        self.jc = 10
        self.right = False
        self.left = False
        self.walk = 0
        self.standing = True
        self.health = 10




    def respawn(self):
        time.sleep(0.4)

        for obj in entities:
            obj.x = (-1*(m.x - obj.x) - 3600)
            obj.y = (-1*(m.y - obj.y) - 3700)

        m.x += (-3600 - m.x)
        m.y += (-3700 - m.y)
        #monster.y += (-1*(m.y - monster.y) - 3700)

    def death(self):
        self.sethealth(10)
        self.respawn()

    def sethealth(self, x):
        self.health = x

    def draw(self,w):

        w.blit(health[self.health], (730, 20))

        if self.walk + 1 >= 27:
            self.walk = 0

        if not(self.standing):
            if self.left:
                 
                w.blit(walkLeft[self.walk//3], (self.x,self.y))
                self.walk += 1
            elif self.right:
                w.blit(walkRight[self.walk//3], (self.x,self.y))
                self.walk += 1
        else:
            if self.left:
                w.blit(walkLeft[0], (self.x,self.y))
            else:
                w.blit(walkRight[0], (self.x,self.y))
