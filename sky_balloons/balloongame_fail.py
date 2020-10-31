import sys

import pygame
import os

# Intialize all pygame modules
pygame.init()

# Size of the screen
SIZE = WIDTH, HEIGHT = 489, 481
# The color of the background if used!
BACKGROUND_COLOR = pygame.Color('black')
# Will be used to remove the color from the background! Must be this color!
PURPLE = (229, 63, 228)
# This depends on hardware! You can have up to 60 based on your refresh rate and hz!
FPS = 60
# The picture for the background image if used
wallpaper = pygame.image.load("wallpaper.png")
# The position of the wallpaper when blit
wallpaper_pos = (0, 0)
# Used to calculate collision
speed = [2, 2]

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


def load_images(path):
    # Image holder, starts empty on purpose
    images = []
    # gets all the images in the specified file for organizational purposes
    for file_name in os.listdir(path):
        image = pygame.image.load(path + os.sep + file_name).convert()
        images.append(image)
    return images


class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, position, images):
        """
        Animated sprite object.

        Args:
            position: x, y coordinate on the screen to place the AnimatedSprite.
            images: Images to use in the animation.
        """
        super(AnimatedSprite, self).__init__()

        size = (32, 32)  # This should match the size of the images.

        self.rect = pygame.Rect(position, size)
        self.movex = 0
        self.movey = 0
        self.images = images
        self.images_right = images
        self.images_left = [pygame.transform.flip(image, True, False) for image in images]  # Flipping every image.
        self.index = 0
        self.image = images[self.index]  # 'image' is the current image of the animation.

        self.velocity = pygame.math.Vector2(0, 0)

        self.animation_time = 0.1
        self.current_time = 0

        self.animation_frames = 6
        self.current_frame = 0

    def update_time_dependent(self, dt):

        # Use the right images if sprite is moving right.
        if self.velocity.x or self.movex > 0:
            self.images = self.images_right

        # Use the left images if the sprite is moving left
        elif self.velocity.x < 0 or self.movey < 0:
            self.images = self.images_left

        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(*self.velocity)

    def control(self, x, y):
        self.movex += x
        self.movey += y

    def update(self, dt):

        # This called to update the sprites realtive to the time
        self.update_time_dependent(dt)


def main():
    images = load_images(path='/Main/sky_balloons'
                              '/time_stone')

    # Provide the full path to the images directory.
    player = AnimatedSprite(position=(100, 100), images=images)
    player_pos = player.get_rect()
    all_sprites = pygame.sprite.Group(player)  # Creates a sprite group and adds 'player' to it.

    running = True
    while running:

        dt = clock.tick(FPS) / 1000  # Amount of seconds between each loop.

        # This is the loop that keeps the game going
        # While the player doesn't exit out the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    running = False
            # When the player presses the down key, move the baloon to the bottom
            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    pygame.quit()
                    try:
                        sys.exit()
                    finally:
                        running = False
                # If it is to the right, then move to the right
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.velocity.x = 4
                # If it is to the left, move the balloon left
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.velocity.x = -4
                # If it is down, move down
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    player.velocity.y = 4
                # If it is up, move up
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    player.velocity.y = -4
                elif player.rect.left < 0 or player.rect.right > WIDTH:
                    player.velocity.x = 0
                    player.velocity.y = 0
                elif player.rect.top < 0 or player.rect.bottom > HEIGHT:
                    player.velocity.y = -4
            if event.type == pygame.KEYUP:
                # If the right or left key is pressed, set velocity to 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player.velocity.x = 0
                # If the down or up key is pressed, set velocity to 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    player.velocity.y = 0
                elif player.rect.left < 0 or player.rect.right > WIDTH:
                    player.velocity.x = 0
                elif player.rect.top < 0 or player.rect.bottom > HEIGHT:
                    player.velocity.y = 0

        # Calls the 'update' method on all sprites in the list (can add more to the group, just player right now).
        all_sprites.update(dt)
        # Colors the background. Use the Blit to use a custom image instead of a color!
        screen.blit(wallpaper, (0, 0))
        all_sprites.draw(screen)
        # This allows the screen to update
        pygame.display.update()


if __name__ == '__main__':
    main()
