import pygame

size = 40

class Snake:
   def __init__(self, parent_screen,length):
        self.parent_screen = parent_screen
        self.length = length
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [size]*length 
        self.y = [size]*length
       

        self.direction ='down'

   def increse_length(self):
       self.length += 1
       self.x.append(-1)
       self.y.append(-1)
       
    
   def draw(self):
        #self.parent_screen.fill((30, 30, 30))
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