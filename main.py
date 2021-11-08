import pygame
from pygame.locals import *

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

TILE_NUMBER = 8

TILE_WIDTH = SCREEN_WIDTH / TILE_NUMBER
TILE_HEIGHT = SCREEN_HEIGHT / TILE_NUMBER

GRID_WIDTH = SCREEN_WIDTH / TILE_WIDTH
GRID_HEIGHT = SCREEN_HEIGHT / TILE_HEIGHT

def drawBoard(surface):
    for y in range(int(GRID_HEIGHT)):
        for x in range(int(GRID_WIDTH)):
            if(x+y) % 2 == 0:
                whiteTile = pygame.Rect((x*TILE_WIDTH, y*TILE_HEIGHT), (TILE_WIDTH,TILE_HEIGHT))
                pygame.draw.rect(surface, (232, 221, 211), whiteTile)
                #surface.blit("Pieces\WhiteKing.png", (x*TILE_WIDTH, y*TILE_HEIGHT))
            else:
                blackTile = pygame.Rect((x*TILE_WIDTH, y*TILE_HEIGHT), (TILE_WIDTH,TILE_HEIGHT))
                pygame.draw.rect(surface, (163, 72, 72), blackTile)
                #surface.blit('\Pieces\WhiteKing.png', (x*TILE_WIDTH, y*TILE_HEIGHT))

def drawPieces(layout):
    # Image = pygame.image.load('/Pieces/WhiteKing.png')
    # gameDisplay.blit(Image, (x,y))
    pass


def main():
    # Initialise screen
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Space Chess')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    #Image = pygame.image.load('/Pieces/WhiteKing.png')

    drawBoard(background)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

     # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()
main()