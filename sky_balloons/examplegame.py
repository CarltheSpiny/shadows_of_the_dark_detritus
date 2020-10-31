import sys
import pygame

# sets the window parameters
width = 500
height = 350

# sets the vars from above to the screen
screen = pygame.display.set_mode((width, height))

# sets the intial speed
speed = [2, 2]
# sets the color of the background
black = 0, 0, 0

# load the image in this directory
ball = pygame.image.load("ball.png")

# get the rect() position
ball_rect = ball.get_rect()

# game loop
running = True
while running:
    # listen for events
    # allows the game to end or continue
    for event in pygame.event.get():
        # terminate game on exit
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    running = False
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                # speed[0] is equal to the x coordinate
                # speed[1] is equal to the y coordinate
                speed[0] = -speed[0]

            if event.key == pygame.K_LEFT or event.key == ord('a'):
                speed[0] = +speed[0]

            if event.key == pygame.K_UP or event.key == ord('w'):
                speed[1] = +speed[1]

            if event.key == pygame.K_UP or event.key == ord('s'):
                speed[1] = -speed[1]
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                speed[0] = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                speed[1] = 0
        if ball_rect.left < 0 or ball_rect.right > width:
            speed[0] = -speed[0]
        if ball_rect.top < 0 or ball_rect.bottom > height:
            speed[1] = -speed[1]

    # update sprite location
    # adds 2 to x and 2 to y
    # .move() allows you to update the rectangle position
    ball_rect = ball_rect.move(speed)
    # if the ball reaches the left(pos 0) or the right value is greater than width
    # same as if the ball reaches the right
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]

    # repaint screen
    screen.fill(black)
    # needs and item and a position
    screen.blit(ball, ball_rect)
    # clears the contents of the entire display
    pygame.display.flip()
