import pygame

pygame.init()

class Figure(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_op = pygame.Surface((110,165))
        self.image_cl = pygame.Surface((110,110))
        self.image_ig = pygame.Surface((55,55))
        self.image = self.image_cl
        self.rect = self.image.get_rect()
        self.tru_rect = self.rect
        self.colided = False
        pygame.draw.rect(self.image,(55,55,55),self.rect)
        pygame.draw.rect(self.image,(0,0,0),self.rect,1)
        pygame.draw.rect(self.image_op,(55,55,55),(0,0,110,165))
        pygame.draw.rect(self.image_op,(0,0,0),(0,0,110,165),1)
        pygame.draw.rect(self.image_cl,(55,55,55),(0,0,110,110))
        pygame.draw.rect(self.image_cl,(0,0,0),(0,0,110,110),1)
        pygame.draw.rect(self.image_ig,(55,55,55),(0,0,55,55))
        pygame.draw.rect(self.image_ig,(0,0,0),(0,0,55,55),1)
        self.cost = 0
        self.name = "карта"
        self.description = "чета делает"
        self.hp = 1
    def action_1(self):
        pass
    def action_2(self):
        pass
    def action_3(self):
        pass        
    def draw(self):
        pass
    def update(self,mouse,screen):
        if self.colided:
            if self.tru_rect.collidepoint(mouse):
                self.rect = (50,350,105,405)
            else:
                self.colided = False
                self.rect = self.tru_rect
        if self.rect.collidepoint(mouse):
            self.colided = True
            self.image = self.image_op
            self.tru_rect = self.rect
            self.rect = (50,350,105,405)
        else:
            self.image = self.image_cl
