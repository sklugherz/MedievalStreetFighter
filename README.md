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


### What I'm Planning on Implementing:

- SinglePlayer
- Basic AI for SinglePlayer
- Map/Background Selection
- Asset Credits/Credit Location
- more characters


### Current Workspace:

- Dynamic Character Selection screen

##### High Prio

##### Current

- fix character select screen layout
  - create new crops of characters for char select
  - guess and check different placement values
  - figure out why P1 text does not cover the selected image
    - maybe its not explicitly being set to the char crop's position

##### BackLogged

- Load fighter data
  - Need to rework how characters are stored
  - list of dictionairs does not suffice, custom data structure needed.

- Add more characters to the database
  - adds data to list of dictionairies, add asset folders, maybe encompass fighter assets into their own folder, add to character select screen, adjust character select game loop to acount for these new characters.
