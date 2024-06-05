import pygame
import random
import time

pygame.init()

win = pygame.display.set_mode((1100, 600))
pygame.display.set_caption("Dino")

Bird = [pygame.image.load('Bird1.png'), pygame.image.load('Bird2.png')]
Cloud = pygame.image.load('cloud.png')
Largecactus = [pygame.image.load('LargeCactus1.png'), pygame.image.load('LargeCactus2.png'), pygame.image.load('LargeCactus3.png')]
Smallcactus = [pygame.image.load('SmallCactus1.png'), pygame.image.load('SmallCactus2.png'), pygame.image.load('SmallCactus3.png')]
Jumping = pygame.image.load('DinoJump.png')
Dead = pygame.image.load('DinoDead.png')
Duck = [pygame.image.load('DinoDuck1.png'), pygame.image.load('DinoDuck2.png')]
Start = pygame.image.load('DinoStart.png')
Gameover = pygame.image.load('GameOver.png')
Reset = pygame.image.load('Reset.png')
Bg = pygame.image.load('Track.png')
Banner = pygame.image.load('banner.png')
Running = [pygame.image.load('DinoRun1.png'), pygame.image.load('DinoRun2.png')]

clock = pygame.time.Clock()

class dino(object):
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.count = 0
        self.space = False
        self.vel = vel
        self.isJump = False
        self.jumpCount = 10
        self.down = False

    def running(self, win):
        if self.count + 1 >= 6:
            self.count = 0
        if self.space:
            win.blit(Running[self.count // 3], (self.x, self.y))
            self.count += 1

    def ducking(self, win):
        if self.count + 1 >= 6:
            self.count = 0
        if self.down:
            win.blit(Duck[self.count // 3], (2, 455))
            self.count += 1
        if self.space:
            win.blit(Running[self.count // 3], (self.x, self.y))
            self.count += 1

class track(object):
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel

    def ground(self, win):
        self.x -= 10
        win.blit(Bg, (self.x, 505))
        win.blit(Bg, (self.x + 2404, 505))

        if abs(self.x) >= 2400:
            self.x = 0

class obstacles(object):
    def __init__(self, x, y, vel):
        self.z = x
        self.t = y
        self.vel = vel

    def lcactus(self, win):
        win.blit(Largecactus[0], (self.z, self.t))
        win.blit(Largecactus[1], (self.z + 1000, self.t))
        win.blit(Largecactus[2], (self.z + 2000, self.t))
        win.blit(Smallcactus[0], (self.z + 3000, 450))
        win.blit(Smallcactus[2], (self.z + 4000, 450))
        win.blit(Smallcactus[1], (self.z + 4500, 450))
        win.blit(Cloud, (600, 300))
        win.blit(Cloud, (200, 300))
        self.z -= self.vel

        if abs(self.z) >= 6000:
            self.z = 1000

def drawingWindow():
    tr.ground(win)
    ob.lcactus(win)
    man.running(win)
    man.ducking(win)
    pygame.display.update()

ob = obstacles(1100, 425, 10)
tr = track(6, 425, 9)
man = dino(6, 420, 15)

run = True
while run:
    clock.tick(45)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if ob.z - man.x < 200 and not man.isJump:  # If obstacle is close and dino is not already jumping
        man.isJump = True
        man.space = True
        man.down = False

    if man.isJump:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.7 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    win.fill((0, 0, 0))
    drawingWindow()

pygame.quit()