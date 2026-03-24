import pygame
import sys
import time
from pygame.locals import *



class Snake:
   def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = 100 
        self.y = 100

        self.direction ='down'
    
   def draw(self):
        self.parent_screen.fill((30, 30, 30))
        self.parent_screen.blit(self.block,(self.x,self.y))
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
       if self.direction =='up':
           self.y -=10
       if self.direction =='down':
           self.y +=10
       if self.direction =='right':
           self.x +=10
       if self.direction =='left':
           self.x -=10
       self.draw()
      
       
       
       
      

class Game:
   def __init__(self):
         pygame.init()
         self.surface = pygame.display.set_mode((1000,500))
         self.surface.fill((30, 30, 30))
         self.snake = Snake(self.surface)
         self.snake.draw()
    

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
        
         self.snake.walk()
         time.sleep(0.2)
   



    



if __name__ == "__main__":
    game = Game()
    game.run()
 
 
    pygame.quit()
    sys.exit()