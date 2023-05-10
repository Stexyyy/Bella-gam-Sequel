import pygame
import time

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 800))

bananastare = pygame.image.load ("silly1.jpg")
brokesad = pygame.image.load("sillyeyesclosed.jpg")
sandwich = pygame.image.load("sandwich.jpg")
bella = pygame.image.load("AFKBella.jpg")
cheese = bananastare.get_rect(topleft = (200,280))
food = sandwich.get_rect(topleft= (100,280))
bruh = brokesad.get_rect(topleft= (500,400))
mom = bella.get_rect(topleft= (500, 400))


def backstory():

  font = pygame.font.SysFont('calibri.ttf', 38)

  for x in range(255):
      screen.fill((255, 255, 255))
      text = font.render('This dog has sad past... (trust)', True, (255-x,255-x,255-x), (255,255,255))
      screen.blit(bananastare, cheese)
      screen.blit(text, (0,100))
      pygame.display.flip()
      time.sleep(20 / 1000)
      
  for x in range(255):
      screen.fill((255, 255, 255))
      text = font.render('This dog was related to the one who has riches and fame', True, (0,0,0), (255,255,255))
      text2 = font.render('But unfortuntely, the one with riches became corrupted', True, (255-x,255-x,255-x), (255,255,255))
      screen.blit(bananastare, cheese)
      screen.blit(bella, mom)
      screen.blit(text, (0,100))
      screen.blit(text2, (0,200))
      pygame.display.flip()
      time.sleep(20 / 1000)
      
      
  for x in range(255):
      screen.fill((255, 255, 255))
      text = font.render('Because of this.. she stole his sandwhich.', True, (0,0,0), (255,255,255))
      text2 = font.render('and he was sad...', True, (255-x,255-x,255-x), (255,255,255))
      screen.blit(brokesad, bruh)
      screen.blit(sandwich, food)
      screen.blit(text, (0,100))
      screen.blit(text2, (0,200))
      pygame.display.flip()
      time.sleep(20 / 1000)
