import pygame
import Objects
import random
import time
import math
import os
from pygame import mixer
pygame.init()


window_width = 1000
window_height = 650
window_size = (window_width, window_height)

# Game Caption
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Space Surfer")

# Game Icon
icon_image = pygame.image.load(os.path.join("Assets", "icon.png"))
pygame.display.set_icon(icon_image)

# Background
background_image = pygame.image.load(os.path.join("Assets", "background.jpg"))
background_image = pygame.transform.scale(background_image, window_size)

# Background Sound
mixer.music.load(os.path.join("Assets", "background.mp3"))
mixer.music.play(-1)

# Small font
font2 = pygame.font.Font('freesansbold.ttf', 24)
font3 = pygame.font.Font('freesansbold.ttf', 16)

# Score
font = pygame.font.Font('freesansbold.ttf', 32)
scoreobj = Objects.Score()
score_value, s_position_x, s_position_y = scoreobj.return_objects()

# Highscore
try:
    with open("scores.txt", "r") as file:
        lines = file.readlines()
        count = 0
        for i in lines:
            i = i.strip()
            i = int(i)
            lines[count] = i
            count += 1
        highscore_value = max(lines)
except:
    highscore_value = 0

# Gameover text
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Spaceship
spaceship_img = pygame.image.load(os.path.join("Assets", "spaceship.png"))
spaceshipobj = Objects.Spaceship(spaceship_img)
spaceship, position_x, position_y, health_value = spaceshipobj.return_object()

# Asteroid
asteroid_img = pygame.image.load(os.path.join("Assets", "asteroid.png"))
asteroidobj = Objects.Asteroid(asteroid_img)
asteroid, a_position_x, a_position_y = asteroidobj.return_object()

# Asteroid 2
asteroid_img = pygame.image.load(os.path.join("Assets", "asteroid.png"))
asteroidobj_2 = Objects.Asteroid(asteroid_img)
asteroid_2, a_position_x_2, a_position_y_2 = asteroidobj_2.return_object()

# Asteroid 3
asteroid_img = pygame.image.load(os.path.join("Assets", "asteroid.png"))
asteroidobj_3 = Objects.Asteroid(asteroid_img)
asteroid_3, a_position_x_3, a_position_y_3 = asteroidobj_3.return_object()

# Bullet
bullet_img = pygame.image.load(os.path.join("Assets", "bullet.png"))
bulletobj = Objects.Bullet(bullet_img)
bullet, b_position_x, b_position_y = bulletobj.return_object()
bullet_state = bulletobj.ready()

# Coin
coin_img = pygame.image.load(os.path.join("Assets", "coin.png"))
coinobj = Objects.Coin(coin_img)
coin, c_position_x, c_position_y = coinobj.return_object()

# Heart 
heart_img = pygame.image.load(os.path.join("Assets", "heart.png"))
heartobj = Objects.Heart(heart_img)
heart, h_position_x, h_position_y = heartobj.return_object()

# Speed Boost
speedboost_img = pygame.image.load(os.path.join("Assets", "speedup.png"))
speedboostobj = Objects.Speedboost(speedboost_img)
speedboost, sb_position_x, sb_position_y = speedboostobj.return_object() 

# Sheild
shield_img = pygame.image.load(os.path.join("Assets", "shield.png"))
shieldobj = Objects.Speedboost(shield_img)
shield, sh_position_x, sh_position_y = shieldobj.return_object()

# Draw Score
def show_score(score_value, x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    window.blit(score, (x, y))

# Draw Highscore
def show_highscore(highscore_value, x, y):
    highscore = font.render("Highscore : " + str(highscore_value), True, (255, 255, 255))
    window.blit(highscore, (x, y))

# Draw Pause/Menu:
def pause_screen():
    pause = over_font.render("SPACE SURFER", True, (255, 255, 255))
    window.blit(pause, (250, 20))

# Draw Health
def show_health(health_value, x, y):
    health = font.render("Health : " + str(health_value), True, (255, 255, 255))
    window.blit(health, (x, y))

# Draw Health with spaceship
def show_health_with_spaceship(health_value, x, y):
    health = font3.render(str(health_value), True, (255, 255, 255))
    window.blit(health, (x, y))

# Draw Speed Level
def show_speed_level(speed_value, x, y):
    speed = font.render("Speed: Level " + str(speed_value), True, (255, 255, 255))
    window.blit(speed, (x, y))

# Draw Sheild Status
def show_shield_status(shield_status, x, y):
    shield_check = font.render("Shield: " + str(shield_status), True, (255, 255, 255))
    window.blit(shield_check, (x, y))

# Draw Object
def draw_object(object, x, y):
    window.blit(object, (x, y))

# Draw Bullet
def shoot(bullet ,x, y):
    global bullet_state
    bullet_state = bulletobj.fire()
    window.blit(bullet, (x + 24, y + 10))

# Draw GameOver Text
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    quit_text = font.render("Press 'r' to play again and 'q' to quit.", True, (255, 255, 255))
    window.blit(over_text, (300, 250))
    window.blit(quit_text,(225,325))

def draw_instruction():
    instructions = font.render("Embark on an incredible space adventure!", True, (255, 255, 255))
    instructions_a = font.render("Pilot your spaceship through a dangerous asteroid field.", True, (255, 255, 255))
    instructions2 = font2.render("Destroy asteroids to boost your score, but watch out! Each collision takes away a", True, (255, 255, 255))
    instructions2_a = font2.render("hefty 20 health points and decreases your speed, and falling asteroids chip away", True, (255, 255, 255))
    instructions2_b = font2.render("5 health points.", True, (255, 255, 255))
    instructions3 = font2.render("Use speed boosters to zoom past danger with increasing speed, collect shield to", True, (255, 255, 255))
    instructions3_a = font2.render("avoid damage from asteroids and collect valuable power-ups to bolster your ship's", True, (255, 255, 255))
    instructions3_b = font2.render("health.", True, (255, 255, 255))
    instructions4 = font2.render("Grab coins along the way to climb the leaderboard and achieve interstellar", True, (255, 255, 255))
    instructions4_a = font2.render("greatness.", True, (255, 255, 255))
    controls = font.render("Controls:", True, (255, 255, 255))
    controls1 = font2.render("Use arrow keys to move and space to shoot.", True, (255, 255, 255))
    controls2 = font2.render("Press 'p' to start or pause the game.", True, (255, 255, 255))
    controls3 = font2.render("Press 'q' to quit the game.", True, (255, 255, 255))
    window.blit(instructions, (10, 100))
    window.blit(instructions_a, (10, 135))
    window.blit(instructions2, (10, 195))
    window.blit(instructions2_a, (10, 230))
    window.blit(instructions2_b, (10, 265))
    window.blit(instructions3, (10, 300))
    window.blit(instructions3_a, (10, 335))
    window.blit(instructions3_b, (10, 370))
    window.blit(instructions4, (10, 405))
    window.blit(instructions4_a, (10, 440))
    window.blit(controls, (10, 480))
    window.blit(controls1, (10, 525))
    window.blit(controls2, (10, 560))
    window.blit(controls3, (10, 595))

# Collision of bullet and asteroid
def isCollision(asteroidX, asteroidY, bulletX, bulletY):
    distance = math.sqrt(math.pow(asteroidX - bulletX, 2) + (math.pow(asteroidY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Collision of spaceship and asteroid
def isCollision2(asteroidX, asteroidY, playerX, playerY):
    distance = math.sqrt(math.pow(asteroidX - playerX, 2) + (math.pow(asteroidY - playerY, 2)))
    if distance < 40:
        return True
    else:
        return False

# Collision of spaceship and coin
def isCollision3(coinX, coinY, playerX, playerY):
    distance = math.sqrt(math.pow(coinX - playerX, 2) + (math.pow(coinY - playerY, 2)))
    if distance < 40:
        return True
    else:
        return False

# Collision of spaceship and heart
def isCollision4(heartX, heartY, playerX, playerY):
    distance = math.sqrt(math.pow(heartX - playerX, 2) + (math.pow(heartY - playerY, 2)))
    if distance < 40:
        return True
    else:
        return False

# Collision of spaceship and speedboost
def isCollision5(speedboostX, speedboostY, playerX, playerY):
    distance = math.sqrt(math.pow(speedboostX - playerX, 2) + (math.pow(speedboostY - playerY, 2)))
    if distance < 40:
        return True
    else:
        return False

# Collision of spaceship and shield
def isCollision6(shieldX, sheildY, playerX, playerY):
    distance = math.sqrt(math.pow(shieldX - playerX, 2) + (math.pow(sheildY - playerY, 2)))
    if distance < 40:
        return True
    else:
        return False

start_time = time.time()
asteroids_drawn = 1

# Game Status
running = True
x_change = 0
y_change = 0
a_y_change = 0
a_y_change_2 = 0
a_y_change_3 = 0
b_y_change = 0
c_y_change = 0
h_y_change = 0
sb_y_change = 0
sh_y_change = 0
score_increase_for_boost = 40
speed_value = 1
score_increase_for_shield = 70
gamepause = True
gameover = False
gamequit = False
asteroidobj_2_status = False
asteroidobj_3_status = False
booster = False
booster_status = False
increment_status = False
collision5_status = False

shield_1 = False
shield_status = False
increment_status_1 = False
collision6_status = False
shield_wear = False
shield_status_1 = "OFF"

# Gameloop
while running:

    window.blit(background_image, (0, 0))
    
    # Pause Screen
    if gamepause:
        pause_screen()
        draw_instruction()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Start button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gamepause = False
                if event.key == pygame.K_q:
                    running = False

    # Game Screen       
    if not gamepause:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Movement keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    button = "left"
                    x_change -= spaceshipobj.move(button)
                elif event.key == pygame.K_RIGHT:
                    button = "right"
                    x_change += spaceshipobj.move(button)

                if event.key == pygame.K_UP:
                    button = "up"
                    y_change -= spaceshipobj.move(button)
                elif event.key == pygame.K_DOWN:
                    button = "down"
                    y_change += spaceshipobj.move(button)

                # Shoot button
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletSound = mixer.Sound(os.path.join("Assets", "laser.wav"))
                        bulletSound.play()
                        b_position_x = position_x
                        b_position_y = position_y
                        shoot(bullet, b_position_x, b_position_y)

                # Pause button
                if event.key == pygame.K_p:
                    gamepause = True
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    button = "released_l"
                    x_change = 0
                elif event.key == pygame.K_RIGHT:
                    button = "released_r"
                    x_change = 0

                if event.key == pygame.K_UP:
                    button = "released_u"
                    y_change = 0
                elif event.key == pygame.K_DOWN:
                    button = "released_d"
                    y_change = 0

            # Game Over:
            if health_value <= 0:
                gameover = True
                file = open("scores.txt", "a")
                file.write(f"{score_value}\n")
                file.close()

                # Reset highscore values
                if score_value > highscore_value:
                    highscore_value = score_value

            while gameover:

                # Stop objects
                x_change = 0
                y_change = 0
                a_y_change = 0
                a_y_change_2 = 0
                a_y_change_3 = 0
                b_y_change = 0
                c_y_change = 0
                h_y_change = 0
                sb_y_change = 0
                sh_y_change = 0
                score_increase_for_boost = 40
                score_increase_for_shield = 70

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gamequit = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            # Reset Score
                            font = pygame.font.Font('freesansbold.ttf', 32)
                            scoreobj = Objects.Score()
                            score_value, s_position_x, s_position_y = scoreobj.return_objects()

                            # Reset Spaceship
                            spaceship_img = pygame.image.load(os.path.join("Assets", "spaceship.png"))
                            spaceshipobj = Objects.Spaceship(spaceship_img)
                            spaceship, position_x, position_y, health_value = spaceshipobj.return_object()

                            # Reset Asteroid
                            asteroid_img = pygame.image.load(os.path.join("Assets", "asteroid.png"))
                            asteroidobj = Objects.Asteroid(asteroid_img)
                            asteroid, a_position_x, a_position_y = asteroidobj.return_object()

                            # Reset Asteroid2
                            asteroid_img = pygame.image.load(os.path.join("Assets", "asteroid.png"))
                            asteroidobj_2 = Objects.Asteroid(asteroid_img)
                            asteroid_2, a_position_x_2, a_position_y_2 = asteroidobj_2.return_object()

                            # Reset Asteroid3
                            asteroid_img = pygame.image.load(os.path.join("Assets", "asteroid.png"))
                            asteroidobj_3 = Objects.Asteroid(asteroid_img)
                            asteroid_3, a_position_x_3, a_position_y_3 = asteroidobj_3.return_object()

                            # Reset Bullet
                            bullet_img = pygame.image.load(os.path.join("Assets", "bullet.png"))
                            bulletobj = Objects.Bullet(bullet_img)
                            bullet, b_position_x, b_position_y = bulletobj.return_object()
                            bullet_state = bulletobj.ready()

                            # Reset Coin
                            coin_img = pygame.image.load(os.path.join("Assets", "coin.png"))
                            coinobj = Objects.Coin(coin_img)
                            coin, c_position_x, c_position_y = coinobj.return_object()

                            # Reset Heart 
                            heart_img = pygame.image.load(os.path.join("Assets", "heart.png"))
                            heartobj = Objects.Heart(heart_img)
                            heart, h_position_x, h_position_y = heartobj.return_object()

                            # Reset SpeedBoost
                            speedboost_img = pygame.image.load(os.path.join("Assets", "speedup.png"))
                            speedboostobj = Objects.Speedboost(speedboost_img)
                            speedboost, sb_position_x, sb_position_y = speedboostobj.return_object() 

                            # Reset Shield
                            shield_img = pygame.image.load(os.path.join("Assets", "shield.png"))
                            shieldobj = Objects.Speedboost(shield_img)
                            shield, sh_position_x, sh_position_y = shieldobj.return_object()

                            # Reset changing positions and game status
                            x_change = 0
                            y_change = 0
                            a_y_change = 0
                            a_y_change_2 = 0
                            a_y_change_3 = 0
                            b_y_change = 0
                            c_y_change = 0
                            h_y_change = 0
                            sb_y_change = 0
                            sh_y_change = 0
                            speed_value = 1
                            score_increase_for_boost = 40
                            score_increase_for_shield = 70

                            asteroidobj_2_status = False
                            asteroidobj_3_status = False
                            asteroids_drawn = 0

                            booster = False
                            booster_status = False
                            increment_status = False
                            collision5_status = False

                            shield_1 = False
                            shield_status = False
                            increment_status_1 = False
                            collision6_status = False
                            shield_wear = False
                            shield_status_1 = "OFF"

                            gameover = False
                            
                        elif event.key == pygame.K_q:
                            gamequit = True
                            gameover = False
            if gamequit:
                running = False  
        
        # SpaceShip Movement
        position_x += x_change
        position_y += y_change

        # Asteroid Movement
        a_y_change = asteroidobj.move()
        a_position_y += a_y_change
        if asteroidobj_2_status:
            a_y_change_2 = asteroidobj_2.move()
            a_position_y_2 += a_y_change_2
        if asteroidobj_3_status:
            a_y_change_3 = asteroidobj_3.move()
            a_position_y_3 += a_y_change_3
        # Asteroid speed increase
        asteroidobj.increase_speed()
        if asteroidobj_2_status:
            asteroidobj_2.increase_speed()
        if asteroidobj_3_status:
            asteroidobj_3.increase_speed()
        # Drawing asteroids again
        if a_position_y >= 600:
            asteroidobj.reset_positon()
            asteroid, a_position_x, a_position_y = asteroidobj.return_object()
            asteroids_drawn += 1
            spaceshipobj.decrease_health_2()
            health_value = spaceshipobj.return_health()
        
        if asteroidobj_2_status:
            if a_position_y_2 >= 600:
                asteroidobj_2.reset_positon()
                asteroid_2, a_position_x_2, a_position_y_2 = asteroidobj_2.return_object()
                asteroids_drawn += 1
                spaceshipobj.decrease_health_2()
                health_value = spaceshipobj.return_health()

        if asteroidobj_3_status:
            if a_position_y_3 >= 600:
                asteroidobj_3.reset_positon()
                asteroid_3, a_position_x_3, a_position_y_3 = asteroidobj_3.return_object()
                asteroids_drawn += 1
                spaceshipobj.decrease_health_2()
                health_value = spaceshipobj.return_health()

        # Coin Movement
        c_y_change = coinobj.move()
        c_position_y += c_y_change
        # Drawing coin again
        if c_position_y >= 600:
            coinobj.reset_positon()
            coin, c_position_x, c_position_y = coinobj.return_object()

        # Bullet Movement
        if b_position_y <= 0:
            b_position_y = 530
            bullet_state = bulletobj.ready()
        if bullet_state == "fire":
            shoot(bullet, b_position_x, b_position_y)
            b_y_change = bulletobj.move()
            b_position_y -= b_y_change
        
        # Heart Movement
        if health_value < 60:
            h_y_change = heartobj.move()
            h_position_y += h_y_change
        # Drawing Heart again:
        if h_position_y >= 600:
            heartobj.reset_positon()
            heart, h_position_x, h_position_y = heartobj.return_object()
        
        # SpeedBoost movement
        if booster:
            if not collision5_status:
                sb_y_change = speedboostobj.move()
                sb_position_y += sb_y_change
        if sb_position_y >= 600:
            booster = False
        # Drawing Speedboost again:
        if sb_position_y >= 600:
            if score_value > score_increase_for_boost:
                speedboostobj.reset_positon()
                speedboost, sb_position_x, sb_position_y = speedboostobj.return_object()
                increment_status = False
        
        # Shield Movement
        if shield_1:
            if not collision6_status:
                sh_y_change = shieldobj.move()
                sh_position_y += sh_y_change
        if sh_position_y >= 600:
            shield_1 = False
        # Drawing Shield again:
        if sh_position_y >= 600:
            if score_value > score_increase_for_shield:
                shieldobj.reset_positon()
                shield, sh_position_x, sh_position_y = shieldobj.return_object()
                increment_status_1 = False

        
        # Collision of bullet and asteroid
        collision = isCollision(a_position_x, a_position_y, b_position_x, b_position_y)
        if collision:
            explosionSound = mixer.Sound(os.path.join("Assets", "explosion.wav"))
            explosionSound.play()
            bulletobj.reset_position()
            bullet_state = bulletobj.ready()
            asteroidobj.reset_positon()
            asteroid, a_position_x, a_position_y = asteroidobj.return_object()
            asteroids_drawn += 1
            scoreobj.increase()
            score_value = scoreobj.return_score()
        
        # Collision of bullet and asteroid2
        if asteroidobj_2_status:
            collision_a = isCollision(a_position_x_2, a_position_y_2, b_position_x, b_position_y)
            if collision_a:
                explosionSound = mixer.Sound(os.path.join("Assets", "explosion.wav"))
                explosionSound.play()
                bulletobj.reset_position()
                bullet_state = bulletobj.ready()
                asteroidobj_2.reset_positon()
                asteroid_2, a_position_x_2, a_position_y_2 = asteroidobj_2.return_object()
                asteroids_drawn += 1
                scoreobj.increase()
                score_value = scoreobj.return_score()

        # Collision of bullet and asteroid3
        if asteroidobj_3_status:
            collision_b = isCollision(a_position_x_3, a_position_y_3, b_position_x, b_position_y)
            if collision_b:
                explosionSound = mixer.Sound(os.path.join("Assets", "explosion.wav"))
                explosionSound.play()
                bulletobj.reset_position()
                bullet_state = bulletobj.ready()
                asteroidobj_3.reset_positon()
                asteroid_3, a_position_x_3, a_position_y_3 = asteroidobj_3.return_object()
                asteroids_drawn += 1
                scoreobj.increase()
                score_value = scoreobj.return_score()
        
        # Collision of spaceship and asteroid
        collision2 = isCollision2(a_position_x, a_position_y, position_x, position_y)
        if collision2:
            explosionSound = mixer.Sound(os.path.join("Assets", "explosion.wav"))
            explosionSound.play()
            asteroidobj.reset_positon()
            asteroid, a_position_x, a_position_y = asteroidobj.return_object()
            asteroids_drawn += 1
            if not shield_wear:
                spaceshipobj.decrease_health()
                spaceshipobj.decrease_speed()
                if speed_value > 1:
                        speed_value -= 1
            if shield_wear:
                    hits += 1
                    if hits >= 2:
                        shield_wear = False
                        shield_status_1 = "OFF"
            health_value = spaceshipobj.return_health()
        
        # Collision of spaceship and asteroid2
        if asteroidobj_2_status:
            collision2_a = isCollision2(a_position_x_2, a_position_y_2, position_x, position_y)
            if collision2_a:
                explosionSound = mixer.Sound(os.path.join("Assets", "explosion.wav"))
                explosionSound.play()
                asteroidobj_2.reset_positon()
                asteroid_2, a_position_x_2, a_position_y_2 = asteroidobj_2.return_object()
                asteroids_drawn += 1
                if not shield_wear:
                    spaceshipobj.decrease_health()
                    spaceshipobj.decrease_speed()
                    if speed_value > 1:
                        speed_value -= 1
                if shield_wear:
                    hits += 1
                    if hits >= 2:
                        shield_wear = False
                        shield_status_1 = "OFF"
                health_value = spaceshipobj.return_health()
        
        # Collision of spaceship and asteroid3
        if asteroidobj_3_status:
            collision2_b = isCollision2(a_position_x_3, a_position_y_3, position_x, position_y)
            if collision2_b:
                explosionSound = mixer.Sound(os.path.join("Assets", "explosion.wav"))
                explosionSound.play()
                asteroidobj_3.reset_positon()
                asteroid_3, a_position_x_3, a_position_y_3 = asteroidobj_3.return_object()
                asteroids_drawn += 1
                if not shield_wear:
                    spaceshipobj.decrease_health()
                    spaceshipobj.decrease_speed()
                    if speed_value > 1:
                        speed_value -= 1
                if shield_wear:
                    hits += 1
                    if hits >= 2:
                        shield_wear = False
                        shield_status_1 = "OFF"
                health_value = spaceshipobj.return_health()

        
        # Collision of spaceship and coin
        collision3 = isCollision3(c_position_x, c_position_y, position_x, position_y)
        if collision3:
            coinSound = mixer.Sound(os.path.join("Assets", "coin.wav"))
            coinSound.play()
            coinobj.reset_positon()
            coin, c_position_x, c_position_y = coinobj.return_object()
            scoreobj.increase()
            score_value = scoreobj.return_score()
        
        # Collision of spaceship and heart
        collision4 = isCollision4(h_position_x, h_position_y, position_x, position_y)
        if collision4:
            heartSound = mixer.Sound(os.path.join("Assets", "heart.wav"))
            heartSound.play()
            heartobj.reset_positon()
            heart, h_position_x, h_position_y = heartobj.return_object()
            spaceshipobj.increase_health()
            health_value = spaceshipobj.return_health()

        # Collision of spaceship and speedboost
        collision5 = isCollision5(sb_position_x, sb_position_y, position_x, position_y)
        if collision5:
            speedupSound = mixer.Sound(os.path.join("Assets", "speedup.mp3"))
            speedupSound.play()
            collision5_status = True
            speedboostobj.reset_positon()
            speedboost, sb_position_x, sb_position_y = speedboostobj.return_object()
            spaceshipobj.increase_speed()
            speed_value += 1
            increment_status = False
        
        # Collision of spaceship and shield
        collision6 = isCollision5(sh_position_x, sh_position_y, position_x, position_y)
        if collision6:
            shieldSound = mixer.Sound(os.path.join("Assets", "shield.wav"))
            shieldSound.play()
            collision6_status = True
            shieldobj.reset_positon()
            shield, sh_position_x, sh_position_y = shieldobj.return_object()
            increment_status_1 = False
            shield_wear = True
            shield_status_1 = "ON"
            hits = 0

        # Boundary Check
        if position_x <= 0:
            position_x = 0
        elif position_x >=936:
            position_x = 936
        
        if position_y <= 0:
            position_y = 0
        elif position_y >=585:
            position_y = 585

        # Drawing Objects on screen
        draw_object(spaceship, position_x, position_y)
        show_health_with_spaceship(health_value, position_x + 15, position_y + 70)
        draw_object(asteroid, a_position_x, a_position_y)
        if score_value > 30:
            asteroidobj_2_status = True
        if asteroidobj_2_status:
            draw_object(asteroid_2, a_position_x_2, a_position_y_2)

        if score_value > 60:
            asteroidobj_3_status = True
        if asteroidobj_3_status:
            draw_object(asteroid_3, a_position_x_3, a_position_y_3)

        draw_object(coin, c_position_x, c_position_y)

        if health_value < 60:
            draw_object(heart, h_position_x, h_position_y)

        if score_value > score_increase_for_boost:
            booster = True
            if not increment_status:
                booster_status = True
                collision5_status = False
        if booster:
            draw_object(speedboost, sb_position_x, sb_position_y)
        if booster_status:
            score_increase_for_boost += 60
            booster_status = False
            increment_status = True
        
        if score_value > score_increase_for_shield:
            shield_1 = True
            if not increment_status_1:
                shield_status = True
                collision6_status = False
        if shield_1:
            draw_object(shield, sh_position_x, sh_position_y)
        if shield_status:
            score_increase_for_shield += 60
            shield_status = False
            increment_status_1 = True


        show_score(score_value, s_position_x, s_position_y)
        show_health(health_value, 800, 10)
        show_highscore(highscore_value, 10, 45)
        show_speed_level(speed_value, 740, 45)
        show_shield_status(shield_status_1, 800, 80)

        if health_value <= 0:
            game_over_text()
    

    pygame.display.update()

pygame.quit()
