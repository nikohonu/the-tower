#include "Game.hpp"

Game::Game() {}

Game::~Game() {}

void Game::init(const char *title, int w, int h, bool fullscreen) {
  int flags = 0;
  if (fullscreen) {
    flags |= SDL_WINDOW_FULLSCREEN;
  }
  if (SDL_Init(SDL_INIT_VIDEO) == 0) {
    std::cout << "Subsystems initialised!\n";
    window = SDL_CreateWindow(title, w, h, flags);
    std::cout << "a!\n";
    if (window) {
      std::cout << "Window created!\n";
    }
    renderer = SDL_CreateRenderer(window, 0);
    if (renderer) {
      SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
      std::cout << "Renderer created!\n";
    }
    isRunning = true;
  } else
    isRunning = false;
}

void Game::handleEvents() {
  SDL_Event event;
  SDL_PollEvent(&event);
  switch (event.type) {
  case SDL_EVENT_QUIT:
    isRunning = false;
    break;
  default:
    break;
  }
}

void Game::update() { cnt++, std::cout << cnt << "\n"; }

void Game::render() {
  SDL_RenderClear(renderer);
  SDL_RenderPresent(renderer);
}

void Game::clean() {
  SDL_DestroyRenderer(renderer);
  SDL_DestroyWindow(window);
  SDL_Quit();
  std::cout << "Game cleaned!\n";
}
