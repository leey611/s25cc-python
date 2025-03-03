import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("my first game")

WHITE = (255, 255, 255)
FPS = 60

def draw_window():
    # fill screen color, draw stuff etc
    WIN.fill(WHITE) # WIN.fill((255, 255, 255))
    pygame.display.update() # update is required to display


def main():
    clock = pygame.time.Clock()
    # run the game until it is terminated
    run = True
    while run:
        clock.tick(FPS) # ensure the framerate is 60 on any machines
        # check events happened during the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False # exit the while loop
        
        draw_window()
        
    pygame.quit() # quit pygame and close the window

if __name__ == "__main__": # make sure the main() will be run when running this file
    main()