#pragma once

#include "SDL3/SDL.h"
#include <SDL3/SDL_main.h>
#include <SDL3/SDL_video.h>
#include <iostream>

class Game {
public:
  Game();
  ~Game();
  void init(const char *title, int w, int h, bool fullscreen);
  void handleEvents();
  void update();
  void render();
  void clean();

  bool running() { return isRunning; }

private:
  int cnt = 0;
  bool isRunning;
  SDL_Window *window;
  SDL_Renderer *renderer;
};
