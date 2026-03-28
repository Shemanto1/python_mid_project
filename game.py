import pygame
import time
from pygame.locals import *

from snake import Snake
from apple import Apple

size = 40

class Game:
   def __init__(self):
         pygame.init()
         self.surface = pygame.display.set_mode((1000,800))
         pygame.display.set_caption("Snake game")
         pygame.mixer.init()
         self.surface.fill((30, 30, 30))
         self.background_music()
         self.snake = Snake(self.surface,2)
         self.snake.draw()
         self.apple =Apple(self.surface)
         self.apple.draw()
    

   def play(self):
    self.background_image()
    self.snake.walk()
    self.apple.draw()
    self.display_score()
    pygame.display.update()


    if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.a,self.apple.b):
        sound=pygame.mixer.Sound("resources/ding.mp3")
        pygame.mixer.Sound.play(sound)
        self.snake.increse_length()
        self.apple.move()
    
    for i in range(2,self.snake.length):
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
            sound=pygame.mixer.Sound("resources/crash.mp3")
            pygame.mixer.Sound.play(sound)
            raise "game over"
    
    if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 800):
            sound=pygame.mixer.Sound("resources/crash.mp3")
            pygame.mixer.Sound.play(sound)
            raise "Hit the boundry error"
          


   def is_collision(self,x1,y1,x2,y2):
       if x1 >= x2 and x1 < x2 +size:
           if y1 >= y2 and y1 < y2 +size:
               return True
       return False
   
   def display_score(self):
       font = pygame.font.SysFont('arial',30)
       score = font.render(f"score: {self.snake.length-2}",True,(200,200,200))
       self.surface.blit(score,(800,10))
   
   
       
   def show_game_over(self):
       self.background_image()
       font = pygame.font.SysFont('arial',30)
       line1 =font.render(f"Game is over!!! your score is : {self.snake.length-2}",True,(255,200,200))
       self.surface.blit(line1,(200,300))
       line2 = font.render(f"To play again press Enter. To exit press Escape!",True,(255,255,255))
       self.surface.blit(line2,(200,350))
       pygame.mixer.music.pause()
       pygame.display.update()

   def reset(self):
         self.snake = Snake(self.surface,2)
         self.apple =Apple(self.surface)
     
    
   def background_music(self):
       pygame.mixer.music.load("resources/background.mp3") 
       pygame.mixer.music.play()


   def background_image(self):
       background = pygame.image.load("resources/background.jpg")
       self.surface.blit(background,(0,0))

       
       
   
   def run(self):
        running = True
        pause =False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        if self.snake.direction != 'down':
                         self.snake.move_up()
                    if event.key == K_DOWN:
                        if self.snake.direction != 'up':
                         self.snake.move_down()
                    if event.key == K_LEFT:
                        if self.snake.direction != 'right':
                         self.snake.move_left()
                    if event.key == K_RIGHT:
                        if self.snake.direction != 'left':
                         self.snake.move_right()
                    if event.key == K_RETURN:
                        self.background_music()
                        pause = False
                    if event.key == K_ESCAPE:
                        running = False


                if event.type == pygame.QUIT:
                    running = False

            try:
               if not pause: 
                 self.play()
            except Exception as e:
                self.show_game_over()
                pause =True
                self.reset()

            time.sleep(.3)   
