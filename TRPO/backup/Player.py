import pygame

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.hp = 30
        self.hand = 4
        self.hand_zone = pygame.Surface((165,550))
        self.image = self.hand_zone
        self.rect_hand = self.hand_zone.get_rect()
        
    def draw(self,screen):
        pygame.draw.rect(screen,(255,255,0),self.rect_hand,3)
