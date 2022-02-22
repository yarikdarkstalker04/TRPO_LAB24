import pygame
pygame.init()

class Board():
    def __init__(self,size_x,size_y):
        self.ceils=pygame.sprite.Group()
        self.image = pygame.Surface((size_x*55,size_y*55))
        for y in range(size_y):
            for x in range(3,size_x+3):
                self.ceils.add(Ceil((x*55,y*55),True))
        self.image.fill((255,255,255))
class Ceil(pygame.sprite.Sprite):
    def __init__(self,pos,isEmpty):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.image = pygame.Surface((55,55))
        self.rect = self.image.get_rect()
        self.color = (0,255,0)
        
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.isEmpty = isEmpty
    def draw_sqr(self,screen,border = 1):
        pygame.draw.rect(screen,self.color,self.rect,border)
    def update(self,mouse):
        if self.rect.collidepoint(mouse):
            self.color = (255,0,0)
        else:
            self.color = (0,255,0)
         
