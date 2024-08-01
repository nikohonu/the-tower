import typing

from inu_musume_engine import Vector2
from inu_musume_engine.draw import draw_circle
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


class Player(GameObject):
    @typing.override
    def ready(self):
        self.position = Vector2(screen.get_width() / 2, screen.get_height() / 2)

    @typing.override
    def process(self, dt: float):
        draw_circle(self.position, 40, "red")
        if Input.is_action_pressed("up"):
            self.position.y -= 300 * dt
        if Input.is_action_pressed("down"):
            self.position.y += 300 * dt
        if Input.is_action_pressed("left"):
            self.position.x -= 300 * dt
        if Input.is_action_pressed("right"):
            self.position.x += 300 * dt


def main():
    player = Player()
    game = Game(actions)
    game.add_object(player)
    game.run()


if __name__ == "__main__":
    main()
