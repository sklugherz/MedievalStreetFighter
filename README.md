## MedievalStreetFighter

A simple medieval themed, arcade-style fighing game.

### Controls

- Player 1
  - Left: A
  - Right: D
  - Jump: W
  - Attack 1: R
  - Attack 2: T

- Player2
  - Left: Left Arrow
  - Right: Right Arrow
  - Jump: Up Arrow
  - Attack 1: NUMPAD 1
  - Attack 2: NUMPAD 2

### Whats Implemented:

- Hit Registration
- Basic Game Loop
- In-Game UI
- Character Movement & Attacks

### What I'm Planning on Implementing:

- Starting Menu
- SinglePlayer
- Basic AI for SinglePlayer
- Character Selection
- Map/Background Selection
- Asset Credits/Credit Location

### Refactor Processes: (An asterick* means currently being refactored for simpler responsibility set)

- Fighter class is responsible for acting as the player controller.
  - This includes character movements and attacks, character animation extraction from sprite sheets, and simple pygame obscurity for updates and drawing.
- Game class is responsible for running the fighting portion of the game. *
  - This includes the initial countdown, drawing the fight scene, and running the main game loop.
- Menu class is responsible for running all menus. *
  - This includes the main menu, character selection, and fight scene selection.
