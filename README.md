# Space Shooter Game

A simple 2D space shooter game built using Python and `pygame`. The player controls a spaceship to shoot incoming enemies, with basic movement and collision detection.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Ideas for Extending the Game](#ideas-for-extending-the-game)
- [License](#license)

## Introduction
This project is a beginner-friendly 2D space shooter game where the player can move their spaceship left and right and shoot at enemies that descend from the top of the screen. The game helps beginners learn basic game development concepts such as rendering, collision detection, and game loop management in `pygame`.

## Features
- Player-controlled spaceship with left and right movement.
- Shooting mechanics with limited bullets.
- Enemies that spawn and descend from the top of the screen.
- Collision detection between bullets and enemies.

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Briqo-org/space-shooter.git
   cd space-shooter
   ```

2. **Install `pygame`**:
   Make sure `pygame` is installed in your Python environment:
   ```bash
   pip install pygame
   ```

3. **Run the game**:
   ```bash
   python space_shooter.py
   ```

## How to Play
- **Move the spaceship**: Use the arrow keys (`←` and `→`) to move left and right.
- **Shoot**: Press the `spacebar` to shoot bullets.
- **Objective**: Shoot as many enemies as possible without letting them reach the bottom of the screen.


## Ideas for Extending the Game
Here are some suggestions to make the game more engaging and complex:

1. **Add Power-Ups**:
   - Include power-ups like extra speed, rapid-fire, or shields that appear randomly and can be collected by the player.

2. **Introduce Different Enemy Types**:
   - Create enemies with varied behavior, such as those that move in zigzag patterns, shoot back at the player, or have more health.

3. **Implement a Scoring System**:
   - Display a score based on how many enemies the player destroys. Add bonuses for consecutive hits or speed.

4. **Include Levels and Difficulty Progression**:
   - Make the game progressively harder by increasing enemy speed, spawn rate, and the number of enemies as the player advances.

5. **Add a Health System**:
   - Implement a health bar for the player so they can take multiple hits before the game ends.

6. **Enhance Graphics and Animations**:
   - Add background images, animations for shooting and explosions, and use sprite sheets for smoother movement.

7. **Background Music and Sound Effects**:
   - Include background music and sound effects for shooting, hits, and explosions for a more immersive experience.

8. **Create a Boss Battle**:
   - Add a boss enemy that appears at the end of a level with unique attack patterns and more health.

9. **Introduce Multiplayer Mode**:
   - Implement local multiplayer so two players can play on the same screen, taking turns or playing cooperatively.

10. **Add a Leaderboard**:
    - Create a system to track and display high scores so players can compete with themselves or others.


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements
- Built with [pygame](https://www.pygame.org/).
- Spaceship and enemy graphics can be created using tools like [Piskel](https://www.piskelapp.com/) or downloaded from [OpenGameArt](https://opengameart.org/).
