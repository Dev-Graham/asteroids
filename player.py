import pygame
from pygame.math import Vector2
from constants import PLAYER_RADIUS

# Assuming CircleShape is a custom class that exists in your project, otherwise use Sprite or other classes
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.position = Vector2(x, y)  # Set the player's position
        self.radius = PLAYER_RADIUS  # Set the radius from the constants file
        self.rotation = 0  # Initial rotation is 0 degrees (facing upwards)

    def triangle(self):
        """Calculate the three points of the triangle based on rotation"""
        forward = Vector2(0, 1).rotate(self.rotation)  # Vector facing the front of the ship
        right = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5  # Vector for ship's side

        # Calculate the 3 points of the triangle (ship shape)
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]

    def draw(self, screen):
        """Draw the player as a triangle on the screen"""
        # Get the triangle points and draw the polygon (triangle)
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width=2)
