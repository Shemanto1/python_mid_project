import pygame
import sys
import time
from pygame.locals import *

size=40

class Apple:
    def __init__(self,parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.a =size*3
        self.b =size*3

    def draw(self):

        self.parent_screen.blit(self.image,(self.a,self.b))
        pygame.display.update()


    

class Snake:
   def __init__(self, parent_screen,length):
        self.parent_screen = parent_screen
        self.length = length
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [size]*length 
        self.y = [size]*length
       

        self.direction ='down'
    
   def draw(self):
        self.parent_screen.fill((30, 30, 30))
        for i in range(self.length):
         self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.update()

   def move_up(self):
       self.direction ='up'

   def move_down(self):
       self.direction ='down'
       
   def move_left(self):
       self.direction ='left'
       
   def move_right(self):
       self.direction ='right'
       
    
   def walk(self):
       for i in range(self.length-1,0,-1):
           self.x[i] = self.x[i-1] 
           self.y[i] = self.y[i-1] 
       
       if self.direction =='up':
           self.y[0] -=size
       if self.direction =='down':
           self.y[0] +=size
       if self.direction =='right':
           self.x[0] +=size
       if self.direction =='left':
           self.x[0] -=size
      
      
       self.draw()
      
       
       
       
      

class Game:
   def __init__(self):
         pygame.init()
         self.surface = pygame.display.set_mode((1000,800))
         self.surface.fill((30, 30, 30))
         self.snake = Snake(self.surface,6)
         self.snake.draw()
         self.apple =Apple(self.surface)
         self.apple.draw()
    

   def play(self):
       
    self.snake.walk()
    self.apple.draw()

    
   def run(self):
        running = True
        while running:
         for event in pygame.event.get():
            if event.type == KEYDOWN:
                 if event.key == K_UP:
                   self.snake.move_up()
                 if event.key == K_DOWN:
                     self.snake.move_down()
                  
                 if event.key ==K_LEFT:
                     self.snake.move_left()
                  
                 if event.key ==K_RIGHT:
                     self.snake.move_right()
                  
           
            
            if event.type == pygame.QUIT:
                running = False
        
         self.play()
         time.sleep(0.3)
   



    



if __name__ == "__main__":
    game = Game()
    game.run()
 
 
    pygame.quit()
    sys.exit()