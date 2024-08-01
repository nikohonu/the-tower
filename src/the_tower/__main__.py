import random
import typing

import inu_musume_engine as inu

# actions: dict[str, list[Key]] = {
#     "up": [Key.KEY_W],
#     "down": [Key.KEY_S],
#     "right": [Key.KEY_D],
#     "left": [Key.KEY_A],
# }


class Tree(inu.sprite.Sprite):
    def __init__(self, position: inu.math.Vector2, group: inu.sprite.Group):
        super().__init__(group)
        self.image = inu.image.load("sprites/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)


class Player(inu.sprite.Sprite):
    def __init__(self, position: inu.math.Vector2, group):
        super().__init__(group)
        self.image = inu.image.load("sprites/player.png").convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.direction = inu.math.Vector2()
        self.speed = 100

    def input(self):
        keys = inu.key.get_pressed()

        if keys[inu.Key.W.value]:
            self.direction.y = -1
        elif keys[inu.Key.S.value]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[inu.Key.D.value]:
            self.direction.x = 1
        elif keys[inu.Key.A.value]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    @typing.override
    def update(self, dt: float):
        self.input()
        self.rect.center += self.direction * self.speed * dt


class CameraGroup(inu.sprite.Group):
    def __init__(self):
        super().__init__()
        self.surface = inu.display.get_surface()

        # camera_offset
        self.offset = inu.math.Vector2()
        self.half_w = self.surface.get_size()[0] // 2
        self.half_h = self.surface.get_size()[1] // 2

        self.ground_surface = inu.image.load("sprites/level.png").convert_alpha()
        self.ground_rect = self.ground_surface.get_rect(topleft=(0, 0))

    def center_target_camera(self, target: inu.Surface):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def custom_draw(self, player):
        self.center_target_camera(player)
        # ground
        ground_position = self.ground_rect.topleft - self.offset
        self.surface.blit(self.ground_surface, ground_position)
        # active elements
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            _ = self.surface.blit(sprite.image, offset_position)


def main():
    _ = inu.init()
    screen = inu.display.set_mode((1280, 720))
    clock = inu.time.Clock()
    running = True
    dt = 0

    # setup
    camera_group = CameraGroup()
    player = Player((640, 360), camera_group)

    for i in range(100):
        random_x = random.randint(0, 1000)
        random_y = random.randint(0, 1000)
        _ = Tree((random_x, random_y), camera_group)

    while running:
        for event in inu.event.get():
            if event.type == inu.QUIT:
                running = False

        _ = screen.fill("#71ddee")

        camera_group.update(dt)
        camera_group.custom_draw(player)

        inu.display.update()
        dt = clock.tick(144) / 1000


if __name__ == "__main__":
    main()
