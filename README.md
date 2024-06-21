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
- Starting Menu
- Character Selection

### What I'm Planning on Implementing:

- SinglePlayer
- Basic AI for SinglePlayer
- Map/Background Selection
- Asset Credits/Credit Location

### Current Workspace:

- fix players not returning to start postions on death
  - To do this need to refactor select character into its own class from menu.
  - ~Need to derive helper file for draw_bg and any other multi-file functions~
- ~fix players not facing eachother during countdown~
  - ~Run an initial check prior to countdown so characters a rendered right direction~
- fix character select screen layout
  - guess and check different values, resize character crops to be bigger
- fix selecting ElvenWarrior as P2 from returning to main menu
  - almost as if something crucial for P2 doesn't get set when EW is selected... Works with DW
  - Only happenes for the first game
  - Works after returning to menu and playing through again
- ~fix location of pygame.mixer~
  - ~got moved over in previous refactor, need to move back to game from menu~
- Add more characters to the database
  - adds data to list of dictionairies, add asset folders, maybe encompass fighter assets into their own folder, add to character select screen, adjust character select game loop to acount for these new characters.
