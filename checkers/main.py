import pygame
from checkers.constants import WIDTH, RED, HEIGHT, SQUARE_SIZE, BLUE
from checkers.game import Game

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('DRAFT')

FPS = 60

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():

    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    
        
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

            if game.winner() != None:
                print(game.winner())
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render('GeeksForGeeks', True, RED, BLUE)
                run = False    
                
        game.update()
    pygame.quit()
main()