import pygame


class Frame:
    def __init__(self, image, duration=80):
        self.image = image
        self.duration = duration


class Animation:
    def __init__(self, *frames):
        self.frames = frames
        self.i = 0
        self._passed = 0

    @property
    def image(self):
        return self.frames[self.i].image

    def start(self):
        self.i = 0
        self._passed = 0

    def update(self, delta):
        if (len(self.frames) <= 1):
            return

        self._passed += delta

        if self._passed >= self.frames[self.i].duration:
            self._passed = 0
            self.i = (self.i + 1) % len(self.frames)


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.anims = {}
        self.current = None
        self.h_flip = False
        self.v_flip = False

    @property
    def image(self):
        image = self.anims[self.current].image
        return pygame.transform.flip(image, self.h_flip, self.v_flip)

    def add_animation(self, name, *frames):
        self.anims[name] = Animation(*frames)

    def play(self, name, force_restart=False):
        if self.current != name or force_restart:
            self.current = name
            self.anims[name].start()

    def update(self, delta):
        self.anims[self.current].update(delta)
