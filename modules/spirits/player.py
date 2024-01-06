# player.py
import pygame
import math

class Player:
    def __init__(self, x, y, key_straight, key_left, key_right) -> None:
        self.x = x
        self.y = y
        self.angle = 0

        self.hit_detection_cooldown = 500
        self.last_hit = 0
        self.body_damage = 30

        self.health = 100
        self.rotation_speed_current = 0
        self.movement_speed_current = 0
        self.movement_speed_max = 10

        self.key_straight = key_straight
        self.key_left = key_left
        self.key_right = key_right

        self.image = pygame.image.load("source/rocket.png")

    def action(self, keys) -> None:
        if keys[self.key_straight] and self.movement_speed_current < self.movement_speed_max:
            self.movement_speed_current += 0.5
        elif self.movement_speed_current > 0:
            self.movement_speed_current -= 0.25

        self.x += int(self.movement_speed_current * math.sin(math.radians(self.angle)))
        self.y += int(self.movement_speed_current * math.cos(math.radians(self.angle)))

        if self.movement_speed_current == 0:
            self.rotation_speed_current = 1.25
        else:
            self.rotation_speed_current = 2.5

        if keys[self.key_left]:
            self.angle += self.rotation_speed_current
        elif keys[self.key_right]:
            self.angle -= self.rotation_speed_current

    def check_collision(self, other_spirit) -> None:
        if self.hit_detection_cooldown < pygame.time.get_ticks() - self.last_hit:
            if self.rect.colliderect(other_spirit.rect):
                self.last_hit = pygame.time.get_ticks()
                self.health -= other_spirit.damage
                other_spirit.health -= self.body_damage
                print(other_spirit.health)
                self.image = pygame.image.load("source/rocket_hit.png")
            else:
                self.image = pygame.image.load("source/rocket.png")

    def update(self) -> None:
        self.image_rotate = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image_rotate.get_rect(center=(self.x, self.y))

    def draw(self, surface) -> None:
        surface.blit(self.image_rotate, self.rect)