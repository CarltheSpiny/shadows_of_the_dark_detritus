import sys
import pygame as pg


def main():
    # This is the vaule of the Screen size
    width, height = 489, 481
    # The hit bot of the ballon/player
    hbox, vbox = 48, 48
    # Intiate the screen
    screen = pg.display.set_mode((width, height))
    # A color
    color = (0, 0, 0)
    # Intialize the clock
    clock = pg.time.Clock()
    # A dummy rectangle for debug
    rect = pg.Rect(300, 220, hbox, vbox)
    # The image for the player
    img = pg.image.load("images/balloon.png")
    # Optimize it
    img.convert()
    # Make it able to accept the x and y
    img_rect = img.get_rect()
    # Set the center of the rect/player
    img_rect.center = width // 2, height // 2
    # Set the background image
    background_1 = pg.image.load("images/wallpaper.png")
    # The tuple for the x, y pos of the background
    background_1_pos = (0, 0)

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        keys = pg.key.get_pressed()

        # booster
        move = 8 if keys[pg.K_LSHIFT] else 4
        if keys[pg.K_q]:
            pg.quit()
        if keys[pg.K_a]:  # to move left
            img_rect.x -= move
        if img_rect.x < 0: img_rect.x = 0

        if keys[pg.K_d]:  # to move right
            img_rect.x += move
        if img_rect.x > width - hbox:
            img_rect.x = width - hbox

        if keys[pg.K_w]:  # to move up
            img_rect.y -= move
        if img_rect.y < 0: img_rect.y = 0

        if keys[pg.K_s]:  # to move down
            img_rect.y += move
        if img_rect.y > height - hbox:
            img_rect.y = height - vbox

        screen.fill((40, 40, 40))
        screen.blit(background_1, background_1_pos)
        screen.blit(img, img_rect)
        # Unused rectangle, debug uses only
        # pg.draw.rect(screen, color, img_rect, 2)
        # pg.draw.rect(screen, (150, 200, 20), rect)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()
