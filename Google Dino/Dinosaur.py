import pygame
import random
import time
pygame.init()

win = pygame.display.set_mode((1100,600))

pygame.display.set_caption("Dino")


Bird = [pygame.image.load('Bird1.png'),pygame.image.load('Bird2.png')]
Cloud = pygame.image.load('cloud.png')
Largecactus = [pygame.image.load('LargeCactus1.png'),pygame.image.load('LargeCactus2.png'),pygame.image.load('LargeCactus3.png')]
Smallcactus = [pygame.image.load('SmallCactus1.png'),pygame.image.load('SmallCactus2.png'),pygame.image.load('SmallCactus3.png')]
Jumping = pygame.image.load('DinoJump.png')
Dead = pygame.image.load('DinoDead.png')
Duck =[pygame.image.load('DinoDuck1.png'),pygame.image.load('DinoDuck2.png')]
Start = pygame.image.load('DinoStart.png')
Gameover = pygame.image.load('GameOver.png') 
Reset = pygame.image.load('Reset.png')
Bg = pygame.image.load('Track.png')
Banner = pygame.image.load('banner.png')
Running = [pygame.image.load('DinoRun1.png'),pygame.image.load('DinoRun2.png')]



clock = pygame.time.Clock()

class dino(object):
    def __init__(self,x,y,vel):  
        self.x = x 
        self.y = y 
        self.count = 0
        self.space = False
        self.vel = vel
        self.isJump = False
        self.jumpCount = 10 
        self.down = False

    def running(self,win):

        if self.count + 1 >= 6:
           self.count = 0
        if self.space:
           win.blit(Running[self.count // 3],(self.x,self.y))
           self.count += 1                                       
    
    def ducking(self,win):
        if self.count + 1 >= 6:
           self.count = 0
        if self.down:
           win.blit(Duck[self.count // 3],(2,455))
           self.count += 1  
        if self.space:
           win.blit(Running[self.count // 3],(self.x,self.y))
           self.count += 1   

    def ai_control(self, obstacle):
        if self.y == 420 and obstacle.z < self.x + 300 and obstacle.z > self.x:
            self.isJump = True
            self.space = True
            self.down = False             

class track(object):
    def __init__(self,x,y,vel):  
        self.x = x 
        self.y = y 
        self.count = 0
        self.right = False
        self.vel = vel
        self.isJump = False
        self.jumpCount = 10

    def ground(self,win):
          
          self.x -= 10
          win.blit(Bg,(self.x,505))
          win.blit(Bg,(self.x + 2404,505))
  
          if abs(self.x) >= 2400:
            self.x = 0

          if self.x >= 2400:
             self.x += 15
          

class obstacles(object):
    def __init__(self,x,y,vel):  
        self.z = x
        self.t = y
        self.count = 0
        self.right = False
        self.vel = vel
        self.isJump = False
        self.jumpCount = 10 
        self.type = type


    def lcactus(self,win):
 
#       self.type= random.randint(200,1000) 

#       if self.type == 0:
       
        win.blit(Largecactus[0],(self.z  ,self.t)) 

        win.blit(Largecactus[1],(self.z + 1000 ,self.t))
            
        win.blit(Largecactus[2],(self.z + 2000 ,self.t))

        win.blit(Smallcactus[0],(self.z + 3000 ,450))

        win.blit(Smallcactus[2],(self.z + 4000 ,450))

        win.blit(Smallcactus[1],(self.z + 4500 ,450))

        win.blit(Cloud,(600,300))

        win.blit(Cloud,(200,300))

        self.z -= self.vel

        if abs(self.z) >= 6000:
            self.z = 1000

class Bird(object):
    def __init__(self,x,y,vel):  
        self.x = x
        self.y = y
        self.count = 0
        self.right = False
        self.vel = vel
        self.isJump = False
        self.jumpCount = 10 
    
    def bird(self,win):
        pass
            

def drawingWindow():
    tr.ground(win)  
    ob.lcactus(win)
    man.running(win)
    man.ducking(win)
    pygame.display.update() 

#def eval_genome(genomes,config):  

  #  global ge,nets                                                                                                                                                                                                                                        

ob = obstacles(1100,425,10)
tr = track(6,425,9)
man = dino(6,420,15)
run = True
while run:
    clock.tick(45)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  

    man.ai_control(ob)
 

    keys = pygame.key.get_pressed()

    if keys [pygame.K_DOWN]:
        man.down = True
        man.space = False
    if not(man.isJump):
        if keys [pygame.K_SPACE]:
            man.isJump = True
            man.space = True
            man.down = False
        
        
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
               neg = -1
            man.y -= (man.jumpCount**2)*0.7*neg
            man.jumpCount -= 1
        
        else:
            man.isJump = False
            man.jumpCount = 10
          
    win.fill((0,0,0)) 
    drawingWindow()
    
    
pygame.quit()

'''
def run(config_path):
    config = neat.config.Config(
          neat.DefaultGenome,
          neat.DefaultReproduction,
          neat.DefaultSpeciesSet,
          neat.DefaultStagnation,
          config_path
        )

        pop = neat.Population(config)
        pop.run(eval_genome, 50)

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir,'config.txt')
    run(config_path) 
   
'''









