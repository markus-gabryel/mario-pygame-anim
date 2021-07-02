import pygame
from anime import Frame, Animation, AnimatedSprite

MARIO_IDLE = pygame.image.load('assets/mario-idle.png')
MARIO_JUMP = pygame.image.load('assets/mario-jump.png')
MARIO_WALK1 = pygame.image.load('assets/mario-walk1.png')
MARIO_WALK2 = pygame.image.load('assets/mario-walk2.png')
MARIO_WALK3 = pygame.image.load('assets/mario-walk3.png')

GRAVITY = 40
JUMP_POWER = 1000
WALKING_SPEED = 200
RUNNING_SPEED = 400


class Mario(AnimatedSprite):
    def __init__(self, screen_size, **rect_args):
        super().__init__()
        self.add_animation('idle', Frame(MARIO_IDLE))
        self.add_animation('jump', Frame(MARIO_JUMP))
        self.add_animation('walk',
                           Frame(MARIO_WALK1),
                           Frame(MARIO_WALK2),
                           Frame(MARIO_WALK3))
        self.add_animation('run',
                           Frame(MARIO_WALK1, 40),
                           Frame(MARIO_WALK2, 40),
                           Frame(MARIO_WALK3, 40))
        self.play('idle')
        self.rect = self.image.get_rect(**rect_args)
        self.velocity = pygame.Vector2(0, 0)
        self.screen_size = screen_size
    
    @property
    def on_ground(self):
        return self.rect.bottom >= self.screen_size[1]

    def walk(self, direction, running=False):
        speed = RUNNING_SPEED if running else WALKING_SPEED
        self.velocity.x = speed * direction

    def jump(self):
        if self.on_ground:
            self.velocity.y -= JUMP_POWER
    
    def _clamp_in_screen(self):
        if self.on_ground:
            self.rect.bottom = self.screen_size[1]

            if self.velocity.y > 0:
                self.velocity.y = 0
    
    def _check_animation(self):
        if self.on_ground:
            if self.velocity.x == 0:
                self.play('idle')
            elif abs(self.velocity.x) == RUNNING_SPEED:
                self.h_flip = self.velocity.x < 0
                self.play('run')
            else:
                self.h_flip = self.velocity.x < 0
                self.play('walk')
        else:
            if self.velocity.x != 0:
                self.h_flip = self.velocity.x < 0
            self.play('jump')

    def update(self, delta):
        super().update(delta)
        self._check_animation()
        self.rect.move_ip(delta / 1000 * self.velocity)
        self.velocity.y += GRAVITY
        self._clamp_in_screen()
