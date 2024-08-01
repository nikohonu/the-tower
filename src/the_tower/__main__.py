import typing

from inu_musume_engine import Vector2, image
from inu_musume_engine.draw import draw_sprite
from inu_musume_engine.game import Game, screen
from inu_musume_engine.game_object import GameObject
from inu_musume_engine.input import Input
from inu_musume_engine.key import Key

actions: dict[str, list[Key]] = {
    "up": [Key.KEY_W],
    "down": [Key.KEY_S],
    "right": [Key.KEY_D],
    "left": [Key.KEY_A],
}


class Level(GameObject):
    @typing.override
    def ready(self):
        self.sprite = image.load("sprites/level.png")

    @typing.override
    def process(self, dt: float):
        draw_sprite(Vector2(0, 0), self.sprite)


class Player(GameObject):
    @typing.override
    def ready(self):
        self.sprite = image.load("sprites/player.png")
        self.position = Vector2(screen.get_width() / 2, screen.get_height() / 2)

    @typing.override
    def process(self, dt: float):
        draw_sprite(self.position, self.sprite)
        if Input.is_action_pressed("up"):
            self.position.y -= 300 * dt
        if Input.is_action_pressed("down"):
            self.position.y += 300 * dt
        if Input.is_action_pressed("left"):
            self.position.x -= 300 * dt
        if Input.is_action_pressed("right"):
            self.position.x += 300 * dt


def main():
    level = Level()
    player = Player()
    game = Game(actions)
    game.add_object(level)
    game.add_object(player)
    game.run()


if __name__ == "__main__":
    main()
