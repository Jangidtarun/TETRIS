import pygame as pg
import random as rn

print("----- BEGIN TETRIS -----")

pg.init()

CELLS = 30
COLS, ROWS = 10, 20
WIDTH, HEIGHT = COLS * CELLS, ROWS * CELLS

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

def main():
    running = True
    while running:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill((0, 0, 0))
        pg.display.flip()

    pg.quit()

main()

print("----- END TETRIS -----")
