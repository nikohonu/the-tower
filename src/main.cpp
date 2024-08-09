#include "Game.hpp"
#include <iostream>

Game *game = nullptr;

int main() {
  game = new Game();
  game->init("the-tower", 800, 600, false);
  while (game->running()) {
    game->handleEvents();
    game->update();
    game->render();
  }

  game->clean();
  return 0;
}
