# Asteroids-PyGame

A simple game of shooting asteroids with a rocket and getting a points

## Requirements

- [pygame](https://www.pygame.org/wiki/GettingStarted)

## Run

### MacOS/Linux

```bash
python3 main.py
```

### Windows

```bash
python main.py
```

## Controls

ESC - escape game

w - up  
d - down  
a - right  
s - left  

space - fire  
r - reload

## States of game

- MENU - until you click on start button
- PLAYING - until you die
- GAME OVER - show best local score

## Objects

### Player

```python
self.angle = 0

self.score = 0

# hit asteroids with your body
self.body_damage = 15

self.health = 100

self.rotation_speed_current = 0
self.movement_speed_current = 2.5
self.movement_speed_max = 10
```

### Projectile

```python
# get angle from rocket
self.angle = angle

self.movement_speed = 25 + speed
self.damage = 15
```

### Asteroids

```python
if self.size == "small":
    self.health = 15
    self.damage = 10
    self.score = 5
elif self.size == "medium":
    self.health = 30
    self.damage = 15
    self.score = 10
elif self.size == "large":
    self.health = 45       
    self.damage = 20
    self.score = 15
```
