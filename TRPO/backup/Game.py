import pygame
from pygame.locals import *
import time
from Board import Board
from Figure import Figure
from Player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((900, 550))
        pygame.display.set_caption('D&F')

        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.generate_board()
        self.generate_player()
        self.generate_hand()
        self.play_game()
    def generate_board(self):
        self.board = Board(10,10)
    def generate_player(self):
        self.player = Player()
    def generate_hand(self):
        self.hand_now = pygame.sprite.Group()
        ceil_x = 1
        ceil_y = -1
        for x in range(self.player.hand):
            card = Figure()
            if x%2:            
                ceil_x=0.5
            else:
                ceil_x=0
                ceil_y+=1
            card.rect.x = (110*ceil_x)
            card.rect.y = (100*ceil_y)
            self.hand_now.add(card)
    def setka_draw(self,mouse):
        self.board.ceils.update(mouse)
        self.board.ceils.draw(self.game_display)
        self.aktiv_ceil = False
        for ceil in self.board.ceils:
            if ceil.color == (255,0,0):
                self.aktiv_ceil = ceil
            else:
                ceil.draw_sqr(self.game_display)
        if self.aktiv_ceil:
            self.aktiv_ceil.draw_sqr(self.game_display,2)
    def draw_hand(self,mouse):
        self.player.draw(self.game_display)
        x = 0
        ceil_y=-1
        for card in self.hand_now:
            if card.colided:
                continue
            if x%2:            
                ceil_x=0.5
            else:
                ceil_x=0
                ceil_y+=1
            card.rect.x = (110*ceil_x)
            card.rect.y = (100*ceil_y)
            x+=1
        self.hand_now.draw(self.game_display)
    def play_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            self.game_display.fill((0,0,0))
            mouse = pygame.mouse.get_pos()
            self.setka_draw(mouse)
            self.draw_hand(mouse)
            self.hand_now.update(mouse,self.game_display)
            self.clock.tick(60)
            pygame.display.flip()
            
if __name__ == '__main__':

    white = (255,255,255)
    blue = (34, 0, 255)
    red = (209, 9, 9)
    black = (0, 0, 0)
    Game()
