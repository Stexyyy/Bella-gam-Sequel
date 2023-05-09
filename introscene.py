import pygame
import time

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 800))

bananastare = pygame.image.load ("silly1.jpg")
brokesad = pygame.image.load("sillyeyesclosed.jpg")
#schmoney = pygame.image.load("images/Schmoney.jpg")
#cheeser = beller.get_rect(topleft = (200,280))
#moner = schmoney.get_rect(topleft= (100,280))
#bruher = schmoney.get_rect(topleft= (100,280))

def backstory():

  font = pygame.font.SysFont('calibri.ttf', 38)

  for x in range(255):
      screen.fill((255, 255, 255))
      text = font.render('This dog has sad past...', True, (255-x,255-x,255-x), (255,255,255))
      screen.blit(bananastare, cheeser)
      screen.blit(text, (0,100))
      pygame.display.flip()
      time.sleep(20 / 1000)
