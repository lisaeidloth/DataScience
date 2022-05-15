import pygame as pg
import os
import random
import time
from Player import Player
from Duck import Duck
from Time import Time

# game constants
SCREENRECT = pg.Rect(0, 0, 640, 480)
FRAME_TARGET = 60
DUCK_SPAWN_RATE = 6 / FRAME_TARGET


def start():
    pg.init()

    screen = pg.display.set_mode(SCREENRECT.size, 0)

    # init sprites
    Player.images = [pg.transform.scale(load_image('player.png'), (50, 50))]  # array for orientation
    Duck.images = [pg.transform.scale(load_image('duck.png'), (52, 36))]

    # game window
    pg.mouse.set_visible(False)
    pg.display.set_caption('Rubber Duck Debugging: Dodge it - if you can!')

    # create the background, tile the bgd image
    b_image = load_image("background.png")
    background = pg.Surface(SCREENRECT.size)
    for x in range(0, SCREENRECT.width, b_image.get_width()):
        background.blit(b_image, (x, 0))
    screen.blit(background, (0, 0))
    pg.display.flip()

    # groups
    ducks = pg.sprite.Group()
    all = pg.sprite.RenderUpdates()

    Player.containers = all
    Duck.containers = all, ducks
    Time.containers = all

    # go
    timer = time.time()
    clock = pg.time.Clock()  # frame limiter

    player = Player(SCREENRECT)
    score = Time(SCREENRECT)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        keystate = pg.key.get_pressed()

        elapsed_time = time.time() - timer
        score.value = elapsed_time

        # clear/erase the last drawn sprites
        all.clear(screen, background)
        all.update()

        # game code here:
        direction = keystate[pg.K_RIGHT] - keystate[pg.K_LEFT]  # 1 - 0 | 0 - 1 | 0 - 0
        player.move(direction)

        # spawn random ducks at random positions
        spawn = random.random() < DUCK_SPAWN_RATE
        if spawn:
            Duck(SCREENRECT)

        # check if a duck hits the player
        for duck in pg.sprite.spritecollide(player, ducks, 1):
            print(f"Spieler wurde getroffen nach: {elapsed_time} Sekunden")
            return

        # draw the scene
        dirty = all.draw(screen)
        pg.display.update(dirty)

        clock.tick(FRAME_TARGET)


def load_image(file):
    file = os.path.join('..', 'assets', file)
    try:
        surface = pg.image.load(file)
        surface.set_colorkey(pg.Color(0, 0, 0))
        surface = surface.convert()
    except pg.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pg.get_error()))
    return surface


if __name__ == '__main__':
    start()
