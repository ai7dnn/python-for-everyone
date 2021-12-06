#%% 프로젝트 Lab 12-pl01-objectorientedpygame.py	파이게임을 객체지향으로 처리 
import pygame
import sys

class PygameMainWindow:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        
    def __drawimage(self):
        self.display.blit(self.image, (10, 10)) 

    def setcaption(self, title):
        pygame.display.set_caption(title)
        
    def setimage(self, imgfname):
        self.image = pygame.image.load(imgfname)

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.__drawimage()        
            pygame.display.update()

mwin = PygameMainWindow(770, 490)
mwin.setcaption('객체지향 방식의 pygame')
mwin.setimage('python.jpg')
mwin.loop()
